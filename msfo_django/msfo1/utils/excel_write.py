from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, numbers


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

