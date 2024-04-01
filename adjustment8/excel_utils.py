from openpyxl import load_workbook
import datetime
from adjustment8.models import Bill, Store, Material, Entrance, Report, EGIL


def create_report(name, date_write_off, date_necessity, date_ig2014):
    id_report, created = Report.objects.get_or_create(name=name, date_write_off=date_write_off,
                                                      date_necessity=date_necessity, date_ig2014=date_ig2014)
    return id_report


def get_report(name):
    report = Report.objects.get(name=name)
    id_report = report.id
    date_write_off = report.date_write_off
    date_necessity = report.date_necessity
    date_ig2014 = report.date_ig2014
    return id_report, date_write_off, date_necessity, date_ig2014


def read_material(line: int, path):
    workbook = load_workbook(f'{path}', read_only=True, data_only=True)
    wb_list = workbook.active
    name = wb_list[f'A{line}'].value
    code = wb_list[f'C{line}'].value
    measuring = wb_list[f'D{line}'].value
    article = wb_list[f'E{line}'].value
    workbook.close()
    return name, code, measuring, article


def read_date(line: int, path):
    workbook = load_workbook(f'{path}', read_only=True, data_only=True)
    wb_list = workbook.active
    line += 2
    date = wb_list[f'A{line}'].value
    date = date_convert(date)
    all_price = wb_list[f'H{line}'].value
    count = wb_list[f'H{line + 1}'].value
    workbook.close()
    if (all_price or count) is None:
        return
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


def write_all_date(line: int, path, report_name):
    id_report, date_write_off, date_necessity, date_ig2014 = get_report(report_name)
    name, code, measuring, article = read_material(line, path)
    material_id, created = Material.objects.get_or_create(name=name, code=code, measuring=measuring, article=article)
    flag = True
    while flag:
        try:
            date, all_price, count = read_date(line, path)
            line += 2
            if all_price is None:
                continue
            price, write_off, reclass, necessity_reserve, ig2014, cost_msfo, write_up, cost_write_off, reserve = (
                entrance_calculation(date, all_price, count, date_write_off, date_necessity, date_ig2014))
            Entrance.objects.create(material_id=material_id, id_report=id_report, id_bill=id_bill, id_store=id_store,
                                    date=date, all_price=all_price, count=count, price=price,
                                    reclass=reclass, write_off=write_off, necessity_reserve=necessity_reserve,
                                    ig2014=ig2014, cost_msfo=cost_msfo, write_up=write_up,
                                    cost_write_off=cost_write_off, reserve=reserve)
        except IndexError:
            flag = False
    return


write_all_date(66, '/home/foile/MSFO/MSFO/static/xlsx/test1001.xlsx')
