from msfo1.utils.util import pull_all_accounts, update_currency_rates_for_year, populate_account_mappings
from msfo1.utils.excel_write import generate_msfo_report
from celery import shared_task


@shared_task()
def crete_report_task(year_report: int):
    populate_account_mappings()
    report_file = pull_all_accounts(year_report)
    update_currency_rates_for_year(year_report)
    generate_msfo_report(year=year_report, report_file=report_file)

