from msfo1.utils.util import pull_all_accounts
from msfo1.utils.excel_write import generate_msfo_report
from celery import shared_task


@shared_task()
def crete_report_task(year_report: int):
    report_file = pull_all_accounts(year_report)
    generate_msfo_report(year=year_report, report_file=report_file)

