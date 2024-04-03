from openpyxl import load_workbook
import datetime
from adjustment8.models import Bill, Store, Material, Entrance, Report, EGIL


class CellException(Exception):
    """Cell value is no correct"""
    pass


def get_or_create_bill(wb_list):
    name = wb_list['A14'].value
    id_bill, created = Bill.objects.get_or_create(name=name)
    return id_bill


def get_or_create_store(line: int, wb_list):
    name = wb_list[f'A{line}'].value
    numbers = wb_list[f'C{line}'].value
    if numbers is None:
        raise CellException
    id_store, created = Store.objects.get_or_create(name=name, numbers=numbers)
    return id_store


def create_report(name, date_write_off, date_necessity, date_ig2014):
    id_report, created = Report.objects.get_or_create(name=name, date_write_off=date_write_off,
                                                      date_necessity=date_necessity, date_ig2014=date_ig2014)
    return id_report


def get_report(name):
    report = Report.objects.get(name=name)
    id_report = report
    date_write_off = report.date_write_off
    date_necessity = report.date_necessity
    date_ig2014 = report.date_ig2014
    return id_report, date_write_off, date_necessity, date_ig2014


def read_material(line: int, wb_list):
    name = wb_list[f'A{line}'].value
    code = wb_list[f'C{line}'].value
    measuring = wb_list[f'D{line}'].value
    return name, code, measuring


def read_date(line: int, wb_list):
    date = wb_list[f'A{line}'].value
    date = date_convert(date)                       # Index error if not correct cell
    all_price = wb_list[f'H{line}'].value
    if all_price is None:
        all_price = 0
    count = wb_list[f'H{line + 1}'].value
    if (all_price or count) is None:
        raise CellException
    return date, all_price, count


def date_convert(date: str):
    date_list = date.split('.')
    date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    return date


def entrance_calculation(date, all_price, count, date_write_off, date_necessity, date_ig2014):
    price = all_price / count

    if date < date_write_off:
        write_off = True                                                # Списываем
    else:
        write_off = False                                               # Не списываем

    if write_off:
        reclass = 4.104
    else:
        reclass = 1.403

    if date_necessity > date and not write_off:
        necessity_reserve = True                                        # Да
    else:
        necessity_reserve = False                                       # Нет

    if date_ig2014 < date:
        ig2014 = 1
    else:
        ig2014 = calculate_ig2014(date)

    if write_off:
        cost_msfo = 0
        write_up = 0
        cost_write_off = all_price - cost_msfo
    else:
        cost_msfo = all_price * ig2014
        write_up = cost_msfo - all_price
        cost_write_off = 0

    if necessity_reserve:
        reserve = cost_msfo
    else:
        reserve = 0
    return price, write_off, reclass, necessity_reserve, ig2014, cost_msfo, write_up, cost_write_off, reserve


def calculate_ig2014(date):
    date = date.replace(day=1)
    egil_obj = EGIL.objects.get(data=date)
    hyper_index = egil_obj.hyper_index
    return hyper_index


def write_all_date(path, report_name):
    print(f'Start func:{datetime.datetime.now()}')
    workbook = load_workbook(f'{path}', data_only=True)
    print(f'Finish load WB:{datetime.datetime.now()}')
    wb_list = workbook.active
    line = 16
    id_report, date_write_off, date_necessity, date_ig2014 = get_report(report_name)
    id_bill = get_or_create_bill(wb_list)
    flag_bill = True
    while flag_bill:
        try:
            id_store = get_or_create_store(line, wb_list)
        except CellException:
            break
        line += 2
        while True:
            name, code, measuring = read_material(line, wb_list)
            if measuring is None:
                break
            id_material, created = Material.objects.get_or_create(name=name, code=code,
                                                                  measuring=measuring)
            line += 2
            flag_material = True
            while flag_material:
                try:
                    date, all_price, count = read_date(line, wb_list)
                    line += 2
                    (price, write_off, reclass, necessity_reserve, ig2014, cost_msfo, write_up, cost_write_off,
                     reserve) = (entrance_calculation(date, all_price, count, date_write_off, date_necessity,
                                                      date_ig2014))
                    Entrance.objects.create(id_material=id_material, id_report=id_report, id_bill=id_bill,
                                            id_store=id_store, date=date, all_price=all_price, count=count, price=price,
                                            reclass=reclass, write_off=write_off, necessity_reserve=necessity_reserve,
                                            ig2014=ig2014, cost_msfo=cost_msfo, write_up=write_up,
                                            cost_write_off=cost_write_off, reserve=reserve)
                except IndexError:
                    flag_material = False
                except ValueError:
                    flag_material = False
                except CellException:
                    line += 2
                    continue
    workbook.close()
    print(f'Finish func:{datetime.datetime.now()}')
    return


create_report(name='2023', date_write_off=datetime.date(2013, 12, 31),
              date_necessity=datetime.date(2020, 12, 31),
              date_ig2014=datetime.date(2015, 1, 1))
Material.objects.all().delete()
Store.objects.all().delete()
write_all_date('/home/foile/MSFO/MSFO/static/xlsx/test1001.xlsx', '2023')
