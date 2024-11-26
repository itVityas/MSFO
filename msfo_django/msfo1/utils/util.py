from msfo1.models import AccountMapping


def populate_account_mappings():
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
