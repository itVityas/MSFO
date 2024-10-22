from .models import Files, Material, Store
from msfo8.excel.utils import fetch_data_from_api, write_all_data_to_db, create_report
from msfo8.excel.excel_write import write_all_date
import datetime
import os
from celery import shared_task

# @shared_task()
# def crete_report_task(year_report):
#     print('step1')
#     path1 = os.path.join('static', 'xlsx', 'file1.xlsx')
#     path2 = os.path.join('static', 'xlsx', 'file2.xlsx')
#
#     print('step2')
#     # Material.objects.all().delete()
#     # Store.objects.all().delete()
#
#     print('step3')
#     create_report(name=year_report, date_necessity=datetime.date(year_report - 2, 12, 31))
#
#     files = Files(year=year_report)
#     files.save()
#
#     write_all_date_bd(f'{path1}', f'{year_report}', files)
#     write_all_date_bd(f'{path2}', f'{year_report}', files)
#
#     print('step4')
#     wb_path = write_all_date(f'{year_report}', f'{year_report}', files)
#
#     # Обновляем экземпляр Files с результатирующим файлом
#     files.result_file = wb_path
#     files.save()
#     print('finish')

@shared_task()
def crete_report_task(year_report: int):

    start_date = f"{year_report}0101"
    end_date = f"{year_report}1231"

    data_list_101 = fetch_data_from_api(start_date, end_date, "101")
    data_list_102 = fetch_data_from_api(start_date, end_date, "102")

    create_report(name=str(year_report), date_necessity=datetime.date(year_report - 2, 12, 31))
    files = Files(year=year_report)
    files.save()

    write_all_data_to_db(data_list_101, str(year_report), files)
    write_all_data_to_db(data_list_102, str(year_report), files)

    wb_path = write_all_date(str(year_report), str(year_report), files)

    files.result_file = wb_path
    files.save()

