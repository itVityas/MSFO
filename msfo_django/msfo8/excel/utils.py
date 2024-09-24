import datetime
from openpyxl import load_workbook
from msfo8.models import Bill, Store, Material, Entrance, Report, Files


class CellException(Exception):
    """Cell value is no correct"""
    pass


def get_or_create_bill(wb_list):
    name = wb_list['A14'].value
    number = name.replace('.', '0')
    id_bill, created = Bill.objects.get_or_create(name=name, number=number)
    return id_bill


def get_or_create_store(line: int, wb_list):
    name = wb_list[f'A{line}'].value
    numbers = wb_list[f'C{line}'].value
    if numbers is None:
        raise CellException
    id_store, created = Store.objects.get_or_create(name=name, numbers=numbers)
    return id_store


def create_report(name, date_necessity):
    id_report, created = Report.objects.get_or_create(name=name, date_necessity=date_necessity)
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
    if count is None:
        raise CellException
    return date, all_price, count


def date_convert(date: str):
    date_list = date.split('.')
    date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    return date


def write_all_date_bd(path, report_name,  id_file: Files):
    wb = load_workbook(f'{path}', data_only=True)
    wb_list = wb.active
    line = 16
    id_report, date_write_off, date_necessity, date_ig2014 = get_report(report_name)
    id_bill = get_or_create_bill(wb_list)
    while True:
        try:
            id_store = get_or_create_store(line, wb_list)
        except CellException:
            break
        line += 2
        while True:
            name, code, measuring = read_material(line, wb_list)
            if measuring is None:
                break
            id_material, created = Material.objects.get_or_create(
                name=name, code=code, measuring=measuring)
            line += 2
            flag_material = True
            while flag_material:
                try:
                    date, all_price, count = read_date(line, wb_list)
                    line += 2
                    Entrance.objects.create(
                        id_material=id_material,
                        id_report=id_report,
                        id_bill=id_bill,
                        id_store=id_store,
                        id_file=id_file,  # Указываем связь с файлом
                        date=date,
                        all_price=all_price,
                        count=count
                    )
                except (IndexError, ValueError):
                    flag_material = False
                except CellException:
                    line += 2
                    continue
    wb.close()


# create_report(name='2023', date_necessity=datetime.date(2021, 12, 31))

# Material.objects.all().delete()
# Store.objects.all().delete()
# write_all_date_bd('/home/foile/MSFO/MSFO/static/xlsx/test1001.xlsx', '2023')
# write_all_date_bd('/home/foile/MSFO/MSFO/static/xlsx/test1002.xlsx', '2023')
