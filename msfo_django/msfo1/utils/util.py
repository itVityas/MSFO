import requests
from datetime import datetime, date
from msfo1.models import AccountMapping, Counterparty, Debt, ReportFile, CurrencyRate
import re




def check_response(response, params):
    """
    Обработка ответа. При пустом/некорректном ответе возвращает none и выводит данные об этом в консоль.
    При корректных данных - возвращает их.
    """
    if not response.text.strip():
        # Если ответ пустой, возвращаем None, выводим параметры запроса и ответа
        print("**************************************************************************************************")
        print("Empty response received, returning None")
        print("--------------------------------------------------------------------------------------------------")
        print(f"Request URL: {response.url}")
        print(f"Request params: {params}")
        print(f"Status code: {response.status_code}")
        print(f"Response text (first 200 chars): {response.text[:200]}")
        print("**************************************************************************************************\n ")
        return None

    try:
        data = response.json()
    except ValueError:
        # Если не удалось распарсить, возвращаем None, выводим параметры запроса и ответа
        print("**************************************************************************************************")
        print("Could not decode JSON, response:")
        print("--------------------------------------------------------------------------------------------------")
        print(f"Request URL: {response.url}")
        print(f"Request params: {params}")
        print(f"Status code: {response.status_code}")
        print(f"Response text (first 200 chars): {response.text[:200]}")
        print("**************************************************************************************************\n ")
        return None

    return data


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
    data = check_response(response, params)
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
        debt_byn = to_float(item.get('СуммаКонечныйОстаток', 0))
        debt_contract_currency = to_float(item.get('ВалютнаяСуммаКонечныйОстаток', '0'))
        contract_currency = item.get('Валюта')
        date_of_debt_str = item.get('Субконто3Дата')
        payment_term_days = int(item.get('СрокОплаты') or 0)

        # Парсим дату
        if date_of_debt_str and date_of_debt_str.strip():
            date_of_debt = datetime.strptime(date_of_debt_str.strip(), '%d.%m.%Y %H:%M:%S').date()
        else:
            date_of_debt = None

        # Проверяем на отрицательные значения
        if debt_byn < 0 or debt_contract_currency < 0:
            # Если хотя бы одно отрицательное, пропускаем запись
            continue

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


def get_distinct_currencies_for_year(year_report):
    """
    Ищет все необходимые валюты
    """
    currencies = (Debt.objects
                  .filter(report_file__year_report=year_report)
                  .values_list('contract_currency', flat=True)
                  .distinct())
    return list(currencies)


def fetch_currency_rate_from_api(currency, date_obj):
    """
    Делает запрос к API с курсом валют.
    Возвращает распарсенные данные, либо None, если ответ пустой или невалидный.
    """
    date_str = date_obj.strftime("%Y%m%d")
    api_url = 'http://192.168.2.2/Arxiv2023test/hs/customs/currency/'
    params = {
        'date': date_str,
        'currency': currency
    }
    auth = ('API', '1')
    response = requests.get(api_url, params=params, auth=auth)
    data = check_response(response, params)
    return data


def save_currency_rate(currency, date_obj, data):
    """
    Сохраняет курс валют в БД.
    """
    if not data:  # Если data=None или data=[]
        return None

    rate = data[0].get('Курс')
    if rate is None:
        return None

    # Если RUB — делим на 100. Если CNY — делим на 10.
    if currency.upper() == 'RUB':
        rate = rate / 100
    elif currency.upper() == 'CNY':
        rate = rate / 10

    obj, created = CurrencyRate.objects.get_or_create(
        currency=currency,
        date=date_obj,
        defaults={'rate': rate}
    )

    if not created:
        obj.rate = rate
        obj.save()

    return obj


def update_currency_rates_for_year(year_report):
    """
    Объединяющая функция для сохранения курса валют в БД.
    Берет все уникальные валюты за указанный год (по данным из Debt),
    проверяет, есть ли курс на 31.12.<year_report>, если нет — тянет с API.
    """
    end_date = date(year_report, 12, 31)

    currencies = get_distinct_currencies_for_year(year_report)

    for currency in currencies:
        if not CurrencyRate.objects.filter(currency=currency, date=end_date).exists():
            rate = fetch_currency_rate_from_api(currency, end_date)
            if rate is not None:
                save_currency_rate(currency, end_date, rate)

