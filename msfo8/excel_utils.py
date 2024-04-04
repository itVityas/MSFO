from openpyxl import load_workbook
import datetime
from msfo8.models import Bill, Store, Material, Entrance, Report, EGIL


class CellException(Exception):
    """Cell value is no correct"""
    pass


def get_or_create_bill(wb_list):
    name = wb_list['A14'].value
    number = name.replace('.', '0')
    id_bill, created = Bill.objects.get_or_create(name=name, number=number)
    return id_bill


def get_or_create_store(line: int, wb_list):
    name = wb_list[f'A{line}'].value
    numbers = wb_list[f'C{line}'].value
    if numbers is None:
        raise CellException
    id_store, created = Store.objects.get_or_create(name=name, numbers=numbers)
    return id_store


def create_report(name, date_write_off, date_necessity, date_ig2014):
    id_report, created = Report.objects.get_or_create(name=name, date_write_off=date_write_off,
                                                      date_necessity=date_necessity, date_ig2014=date_ig2014)
    return id_report


def get_report(name):
    report = Report.objects.get(name=name)
    id_report = report
    date_write_off = report.date_write_off
    date_necessity = report.date_necessity
    date_ig2014 = report.date_ig2014
    return id_report, date_write_off, date_necessity, date_ig2014


def read_material(line: int, wb_list):
    name = wb_list[f'A{line}'].value
    code = wb_list[f'C{line}'].value
    measuring = wb_list[f'D{line}'].value
    return name, code, measuring


