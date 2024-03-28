from openpyxl import load_workbook
import datetime
from adjustment8.models import Bill, Store, Material, Entrance


def date_convert(date: str):
    date_list = date.split('.')
    date = datetime.date(int(date_list[2]), int(date_list[1]), int(date_list[0]))
    return date


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


def entrance_calculation():
    return


def read_all_date(line: int, path):
    name, code, measuring, article = read_material(line, path)
    material_id, created = Material.objects.get_or_create(name=name, code=code, measuring=measuring, article=article)
    flag = True
    while flag:
        try:
            date, all_price, count = read_date(line, path)
            line += 2
            if all_price is None:
                continue
            # Entrance.objects.create(material_id=material_id, id_report=id_report, id_bill=id_bill, id_store=id_store,
            #                         date=date, all_price=all_price, count=count, price=price,
            #                         reclass=reclass, write_off=write_off, necessity_reserve=necessity_reserve,
            #                         ig2014=ig2014, cost_msfo=cost_msfo, write_up=write_up,
            #                         cost_write_off=cost_write_off, reserve=reserve)
        except IndexError:
            flag = False

    return


read_all_date(66, '/home/foile/MSFO/MSFO/static/xlsx/test1001.xlsx')
