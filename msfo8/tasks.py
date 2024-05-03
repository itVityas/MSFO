from .models import Files, Material, Store
from msfo8.excel.utils import write_all_date_bd, create_report
from msfo8.excel.excel_write import write_all_date
import datetime
import shutil
import os
from celery import shared_task


@shared_task()
def crete_report_task(year_report):
    print('step1')
    path1 = os.path.join('static', 'xlsx', 'file1.xlsx')
    path2 = os.path.join('static', 'xlsx', 'file2.xlsx')

    print('step2')
    Material.objects.all().delete()
    Store.objects.all().delete()

    print('step3')
    create_report(name=year_report, date_necessity=datetime.date(year_report - 2, 12, 31))
    write_all_date_bd(f'{path1}', f'{year_report}')
    write_all_date_bd(f'{path2}', f'{year_report}')

    print('step4')
    wb_path = write_all_date(f'{year_report}', f'{year_report}')
    files = Files(year=year_report, result_file=wb_path)
    files.save()
    print('finish')
