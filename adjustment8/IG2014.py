from adjustment8.models import EGIL


def read_ig2014(line: int, workbook):
    wb_list = workbook.active
    date_ig = wb_list[f'C{line}'].value.date()
    month_index_ig = wb_list[f'D{line}'].value
    year_index_ig = wb_list[f'E{line}'].value
    start_hyper_index_ig = wb_list[f'F{line}'].value
    hyper_index_ig = wb_list[f'H{line}'].value
    flag_ig = True
    if hyper_index_ig == 1:
        flag_ig = False
    return date_ig, month_index_ig, year_index_ig, start_hyper_index_ig, hyper_index_ig, flag_ig


def write_ig2014():
    x = 7
    flag = True
    while flag:
        date, month_index, year_index, start_hyper_index, hyper_index, flag = read_ig2014(x, wb)
        q = EGIL(data=date, month_index=month_index, year_index=year_index, start_hyper_index=start_hyper_index,
                 hyper_index=hyper_index)
        q.save()
        x += 1
    return

