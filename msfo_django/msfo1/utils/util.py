import requests
from datetime import datetime
from msfo1.models import AccountMapping, Counterparty, Debt, ReportFile
import re


def fetch_data(start_date, end_date, account_1c, sorting_number):
    api_url = 'http://192.168.2.2/Arxiv2023test/hs/customs/oborot62/'
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'account': account_1c,
        'type': sorting_number,
    }
    auth = ('API', '1')
    response = requests.get(api_url, params=params, auth=auth)

    if not response.text.strip():
        # Если ответ пустой, возвращаем None, выводим параметры запроса и ответа
        print("\n************************************************************")
        print("Empty response received, returning None")
        print("------------------------------------------------------------")
        print("Request URL:", response.url)
        print("Request params:", params)
        print("Status code:", response.status_code)
        print("Response text (first 200 chars):")
        print(response.text[:200])
        print("************************************************************")
        return None

    try:
        data = response.json()
    except ValueError:
        # Если не удалось распарсить, возвращаем None, выводим параметры запроса и ответа
        print("\n************************************************************")
        print("Could not decode JSON, response:")
        print("------------------------------------------------------------")
        print("Request URL:", response.url)
        print("Request params:", params)
        print("Status code:", response.status_code)
        print("Response text (first 200 chars):")
        print(response.text[:200])
        print("************************************************************")
        return None

    return data



# Сохраняем данные в БД
def save_debts_to_db(data, account_1c, sorting_number, report_file):
    """
    Сохраняет данные в БД
    """
    if not data:  # Если data=None или data=[]
        return

    # Получаем AccountMapping
    try:
        account_mapping = AccountMapping.objects.get(account_1c=account_1c, sorting_number=sorting_number)
    except AccountMapping.DoesNotExist:
        print(f"Не найдено соответствие для счёта {account_1c} с номером сортировки {sorting_number}")
        return

    for item in data:
        # Получаем или создаём контрагента
        counterparty_name = item.get('Субконто1ГоловнойКонтрагентНаименование')
        counterparty, _ = Counterparty.objects.get_or_create(name=counterparty_name)

        # Получаем необходимые поля
        debt_byn = to_float(item.get('СуммаОстатокДт', 0))
        debt_contract_currency = to_float(item.get('ВалютнаяСуммаОстатокДт', '0'))
        contract_currency = item.get('Валюта')
        date_of_debt_str = item.get('Субконто3Дата')
        payment_term_days = int(item.get('СрокОплаты') or 0)

        # Парсим дату
        if date_of_debt_str != 0:
            date_of_debt = datetime.strptime(date_of_debt_str, '%Y-%m-%dT%H:%M:%S').date()
        else:
            date_of_debt = None

        # Создаём и сохраняем объект Debt
        debt = Debt(
            counterparty=counterparty,
            account=account_mapping,
            report_file=report_file,
            debt_byn=debt_byn,
            debt_contract_currency=debt_contract_currency,
            contract_currency=contract_currency,
            date_of_debt=date_of_debt,
            payment_term_days=payment_term_days,
        )
        debt.save()


def to_float(value, default=0.0):
    """
    Переводит значение во float
    """
    if value is None or value == '':
        return default
    value = str(value)
    value = value.replace(',', '.')
    value = re.sub(r'\s+', '', value)
    try:
        return float(value)
    except ValueError:
        print(value)
        return default


def pull_all_accounts(year):
    """
    Загружает данные в БД по всем счетам из AccountMapping за указанный год.
    """
    start_date = f"{year}0101"
    end_date = f"{year}1231"

    accounts = AccountMapping.objects.all()
    report_file = ReportFile.objects.create(year_report=year)

    for account_mapping in accounts:
        account_1c = account_mapping.account_1c
        sorting_number = account_mapping.sorting_number

        data = fetch_data(start_date=start_date,
                          end_date=end_date,
                          account_1c=account_1c,
                          sorting_number=sorting_number)

        save_debts_to_db(data=data,
                         account_1c=account_1c,
                         sorting_number=sorting_number,
                         report_file=report_file)
    return report_file


def populate_account_mappings():
    """
    Заполняет таблицу в БД соотношением счетов в отчете с сортировкой и счетом в 1С
    """
    mappings = [
        {'account_1c': '621', 'db_account_number': '6201', 'sorting_number': '_1'},
        {'account_1c': '621', 'db_account_number': '6217', 'sorting_number': '_6'},
        {'account_1c': '621', 'db_account_number': '6214', 'sorting_number': '_7'},
        {'account_1c': '629', 'db_account_number': '6204', 'sorting_number': '_8'},
        {'account_1c': '6210', 'db_account_number': '6205', 'sorting_number': '_0'},
        {'account_1c': '6211', 'db_account_number': '6201', 'sorting_number': '_1'},
        {'account_1c': '6213', 'db_account_number': '6206', 'sorting_number': '_4'},
        {'account_1c': '6218', 'db_account_number': '6210', 'sorting_number': '_0'},
        {'account_1c': '6219', 'db_account_number': '6212', 'sorting_number': '_0'},
        {'account_1c': '6220', 'db_account_number': '6213', 'sorting_number': '_2'},
        {'account_1c': '6221', 'db_account_number': '6225', 'sorting_number': '_9'},
        {'account_1c': '6222', 'db_account_number': '6225', 'sorting_number': '_9'},
        {'account_1c': '6225', 'db_account_number': '6253', 'sorting_number': '_5'},
        {'account_1c': '6226', 'db_account_number': '6213', 'sorting_number': '_2'},
        {'account_1c': '6227', 'db_account_number': '6238', 'sorting_number': '_0'},
        {'account_1c': '6230', 'db_account_number': '6230', 'sorting_number': '_0'},
        {'account_1c': '6231', 'db_account_number': '6220', 'sorting_number': '_10'},
        {'account_1c': '6233', 'db_account_number': '6233', 'sorting_number': '_0'},
        {'account_1c': '6251', 'db_account_number': '6213', 'sorting_number': '_2'},
        {'account_1c': '6291', 'db_account_number': '6204', 'sorting_number': '_8'},
    ]

    for mapping in mappings:
        AccountMapping.objects.get_or_create(
            account_1c=mapping['account_1c'],
            sorting_number=mapping['sorting_number'],
            defaults={'db_account_number': mapping['db_account_number']}
        )
