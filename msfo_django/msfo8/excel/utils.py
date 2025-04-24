import datetime
from msfo8.models import Bill, Store, Material, Entrance, Report, Files
import requests
from typing import List, Dict
import re
from django.conf import settings


# def fetch_data_from_api(start_date: str, end_date: str, account: str) -> List[Dict]:
def fetch_data_from_api(period: str, account: str) -> List[Dict]:
    url = "http://192.168.2.2/OLYA/hs/customs/oborot/"
    params = {
        # 'startDate': start_date,
        # 'endDate': end_date,
        'account': account,
        'period': period
    }
    auth = (settings.API_USERNAME, settings.API_PASSWORD)
    response = requests.get(url, params=params, auth=auth)
    response.raise_for_status()
    data = response.json()
    return data


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


def write_all_data_to_db(data_list: List[Dict], report_name: str, id_file: Files):
    id_report, date_write_off, date_necessity, date_ig2014 = get_report(report_name)

    for data in data_list:

        bill_name = data.get("Счет").strip()
        bill_number = data.get("Счет").replace('.', '0').strip()
        id_bill, _ = Bill.objects.get_or_create(
            name=bill_name,
            number=bill_number
        )

        store_name = data.get("Субконто2").strip()
        store_numbers = data.get("Субконто2Код").strip()
        id_store, _ = Store.objects.get_or_create(
            name=store_name,
            numbers=store_numbers
        )

        material_name = data.get("Субконто1").strip()
        material_code = int(data.get("Субконто1Код").strip())
        measuring = data.get("Субконто1ЕдиницаИзмерения").strip()

        id_material, _ = Material.objects.get_or_create(
            name=material_name,
            code=material_code,
            measuring=measuring
        )

        date_str = data.get("Субконто3Дата")
        count_str = str(data.get("КоличествоОборотДт")).replace(',', '.')
        count_str = re.sub(r'\s+', '', count_str)
        all_price_str = str(data.get("БУОборотДт")).replace(',', '.')
        all_price_str = re.sub(r'\s+', '', all_price_str)

        date = datetime.datetime.strptime(date_str, "%d.%m.%Y").date()
        count = float(count_str)
        all_price = float(all_price_str)

        Entrance.objects.create(
            id_material=id_material,
            id_report=id_report,
            id_bill=id_bill,
            id_store=id_store,
            id_file=id_file,
            date=date,
            all_price=all_price,
            count=count
        )

