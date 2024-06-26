from msfo8.models import EGIL
from openpyxl import load_workbook


def read_ig2014(line: int, wb_list):
    date_ig = wb_list[f'C{line}'].value.date()
    month_index_ig = wb_list[f'D{line}'].value
    year_index_ig = wb_list[f'E{line}'].value
    start_hyper_index_ig = wb_list[f'F{line}'].value
    hyper_index_ig = wb_list[f'H{line}'].value
    flag_ig = True
    if hyper_index_ig == 1:
        flag_ig = False
    return date_ig, month_index_ig, year_index_ig, start_hyper_index_ig, hyper_index_ig, flag_ig


def write_ig2014(path):
    workbook = load_workbook(f'{path}', data_only=True)
    wb_list = workbook.active
    line = 7
    flag = True
    while flag:
        date, month_index, year_index, start_hyper_index, hyper_index, flag = read_ig2014(line, wb_list)
        EGIL.objects.create(data=date, month_index=month_index, year_index=year_index,
                            start_hyper_index=start_hyper_index, hyper_index=hyper_index)
        line += 1
    workbook.close()
    return


EGIL.objects.all().delete()

write_ig2014('/home/foile/MSFO/MSFO/static/xlsx/IG2014.xlsx')
