import requests
from datetime import datetime
from msfo1.models import AccountMapping, Counterparty, Debt


def fetch_data(start_date, end_date, account_param, type_param):
    """
    Тянет данные из апи
    """
    api_url = 'http://192.168.2.2/OLYA/hs/customs/oborot62_1/'
    params = {
        'startDate': start_date,
        'endDate': end_date,
        'account': account_param,
        'type': f'_{type_param}'
    }
    auth = ('API', '1')
    response = requests.get(api_url, params=params, auth=auth)
    data = response.json()
    return data


# Сохраняем данные в БД
def save_debts_to_db(data, account_param, type_param):
    """
    Сохраняет данные в БД
    """
    if data is None:
        print(f"In account {account_param} no data to save")
        return

    sorting_number = int(type_param.strip('_'))
    account_1c = f"{account_param[:2]}.{account_param[2:]}"

    # Получаем AccountMapping
    try:
        account_mapping = AccountMapping.objects.get(account_1c=account_1c, sorting_number=sorting_number)
    except AccountMapping.DoesNotExist:
        print(f"Не найдено соответствие для счёта {account_1c} с номером сортировки {sorting_number}")
        return

    for item in data:
        # Получаем или создаём контрагента
        counterparty_name = item.get('Субконто1Контрагент')
        counterparty, _ = Counterparty.objects.get_or_create(name=counterparty_name)

        # Получаем необходимые поля
        debt_byn = float(item.get('СуммаОборотДт', 0))
        debt_contract_currency = float(item.get('ВалютнаяСуммаОборотДт', 0))
        contract_currency = item.get('Валюта')
        date_of_debt_str = item.get('Субконто2Дата')
        payment_term_days = int(item.get('СрокОплаты', 0))

        # Парсим дату
        date_of_debt = datetime.strptime(date_of_debt_str, '%Y-%m-%dT%H:%M:%S').date()

        # Создаём и сохраняем объект Debt
        debt = Debt(
            counterparty=counterparty,
            account=account_mapping,
            debt_byn=debt_byn,
            debt_contract_currency=debt_contract_currency,
            contract_currency=contract_currency,
            date_of_debt=date_of_debt,
            payment_term_days=payment_term_days,
        )
        debt.save()


def populate_account_mappings():
    """
    Заполняет таблицу в БД соотношением счетов в отчете с сортировкой и счетом в 1С
    """
    mappings = [
        {'account_1c': '62.1', 'db_account_number': '6201', 'sorting_number': 1},
        {'account_1c': '62.1', 'db_account_number': '6217', 'sorting_number': 6},
        {'account_1c': '62.1', 'db_account_number': '6214', 'sorting_number': 7},
        {'account_1c': '62.9', 'db_account_number': '6204', 'sorting_number': 8},
        {'account_1c': '62.10', 'db_account_number': '6205', 'sorting_number': 0},
        {'account_1c': '62.11', 'db_account_number': '6201', 'sorting_number': 1},
        {'account_1c': '62.13', 'db_account_number': '6206', 'sorting_number': 4},
        {'account_1c': '62.18', 'db_account_number': '6210', 'sorting_number': 0},
        {'account_1c': '62.19', 'db_account_number': '6212', 'sorting_number': 0},
        {'account_1c': '62.20', 'db_account_number': '6213', 'sorting_number': 2},
        {'account_1c': '62.21', 'db_account_number': '6225', 'sorting_number': 9},
        {'account_1c': '62.22', 'db_account_number': '6225', 'sorting_number': 9},
        {'account_1c': '62.25', 'db_account_number': '6253', 'sorting_number': 5},
        {'account_1c': '62.26', 'db_account_number': '6213', 'sorting_number': 2},
        {'account_1c': '62.27', 'db_account_number': '6238', 'sorting_number': 0},
        {'account_1c': '62.30', 'db_account_number': '6230', 'sorting_number': 0},
        {'account_1c': '62.31', 'db_account_number': '6220', 'sorting_number': 10},
        {'account_1c': '62.33', 'db_account_number': '6233', 'sorting_number': 0},
        {'account_1c': '62.51', 'db_account_number': '6213', 'sorting_number': 2},
        {'account_1c': '62.91', 'db_account_number': '6204', 'sorting_number': 8},
    ]

    for mapping in mappings:
        AccountMapping.objects.get_or_create(
            account_1c=mapping['account_1c'],
            sorting_number=mapping['sorting_number'],
            defaults={'db_account_number': mapping['db_account_number']}
        )
