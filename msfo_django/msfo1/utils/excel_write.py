from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, numbers
from msfo1.models import Debt


def set_column_widths(ws):
    """
    Устанавливает ширину столбцов, высоту строки с заголовками
    """
    column_widths = {
        'A': 97.14,
        'B': 12.14,
        'C': 18.43,
        'D': 16.00,
        'E': 13.71,
        'F': 16.71,
        'G': 18.29,
        'H': 17.29,
        'I': 14.71,
        'J': 80.57,
        'K': 15.29,
        'L': 45.14,
        'M': 14.71,
        'N': 25.86,
        'O': 16.29,
        'P': 16.57,
        'Q': 16.57
    }

    for column, width in column_widths.items():
        ws.column_dimensions[column].width = width
    ws.row_dimensions[2].height = 30


def set_font(ws):
    """
    Устанавливает шрифт на всем листе
    """
    font = Font(name='Arial', size=9)
    for row in ws.iter_rows(values_only=False):
        for cell in row:
            cell.font = font


def set_headers(ws, report_date):
    """
    Заполняет заголовки
    """
    headers = [
        "Контрагент",
        "Счет БСУ",
        "Задолженность в белорусских рублях",
        "Задолженность в валюте договора",
        "Валюта договора",
        "Дата возникновения задолженности",
        "Контрактные сроки погашения задолженности",
        "Контрактные сроки погашения задолженности",
        "Количество дней просрочки",
        "Примечание",
        "Счет МСФО",
        "Характер задолженности",
        "Курс валюты на 31.12.2023",
        "Задолженность в белорусских рублях по курсу 31.12.2023",
        "Курсовые разницы",
        "% резервирования",
        "Сумма резерва по номиналу"
    ]

    for col_idx, header in enumerate(headers, start=1):
        ws.cell(row=2, column=col_idx, value=header)
        ws.cell.alignment = Alignment(horizontal="center", vertical='center', wrap_text=True)

    ws.cell(row=1, column=9, value=report_date)


def fill_data_for_account_number(ws, db_account_number):
    """
    Заполнение .xlsx файла данными из бд, формулами
    """

    debts = Debt.objects.filter(account__db_account_number=db_account_number)

    current_row = 3

    for debt in debts:
        ws.cell(row=current_row, column=1, value=debt.counterparty.name)  # A
        ws.cell(row=current_row, column=2, value=debt.account.db_account_number)  # B
        ws.cell(row=current_row, column=3, value=debt.debt_byn)  # С
        if debt.contract_currency == 'BYN':
            ws.cell(row=current_row, column=4, value=debt.debt_byn)  # D
        else:
            ws.cell(row=current_row, column=4, value=debt.debt_contract_currency)  # D
        ws.cell(row=current_row, column=5, value=debt.contract_currency)  # E
        ws.cell(row=current_row, column=6, value=debt.date_of_debt)  # F
        ws.cell(row=current_row, column=7, value=debt.payment_term_days)  # G
        ws.cell(row=current_row, column=8, value=f'=F{current_row}+G{current_row}')
        ws.cell(row=current_row, column=9, value=f'=ЕСЛИ(H{current_row}>$I$1;0;$I$1-H{current_row})')
        ws.cell(row=current_row, column=10, value=f'')
        ws.cell(row=current_row, column=11, value=1.314)
        ws.cell(row=current_row, column=12, value=f'монетарная')
        ws.cell(row=current_row, column=13, value=f'=ЕСЛИ(E{current_row}="BYN";1;"см")')
        ws.cell(row=current_row, column=14, value=f'=M{current_row}*D{current_row}')
        ws.cell(row=current_row, column=15, value=f'=N{current_row}-C{current_row}')
        ws.cell(row=current_row, column=16, value=f"=ЕСЛИ(ИЛИ(K{current_row}=1,314;K{current_row}=4,104);0;ЕСЛИ(I{current_row}>365;100%;ВПР(I{current_row};'% резервирования'!$A$3:$B$369;2;0)))")
        ws.cell(row=current_row, column=17, value=f'=P{current_row}*N{current_row}')

        current_row += 1