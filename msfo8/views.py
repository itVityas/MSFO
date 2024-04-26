from django.shortcuts import render, redirect
from .models import Files, Material, Store
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from msfo8.excel.utils import write_all_date_bd, create_report
from msfo8.excel.excel_write import write_all_date
import datetime
import shutil
import os


def home(request):
    return render(request, 'msfo8/home.html')


def upload_files(request):
    if request.method == 'POST':

        try:
            year_report = int(request.POST.get('year_report'))
            if 1980 > year_report or 2100 < year_report:
                raise ValueError

            file1 = request.FILES.get('file1')
            file2 = request.FILES.get('file2')

            path1 = os.path.join('static', 'xlsx', 'file1.xlsx')
            with open(path1, 'wb') as file:
                for chunk in file1.chunks():
                    file.write(chunk)

            path2 = os.path.join('static', 'xlsx', 'file2.xlsx')
            with open(path2, 'wb') as file:
                for chunk in file2.chunks():
                    file.write(chunk)

            Material.objects.all().delete()
            Store.objects.all().delete()

            create_report(name=year_report, date_necessity=datetime.date(year_report-2, 12, 31))
            write_all_date_bd(f'{path1}', f'{year_report}')
            write_all_date_bd(f'{path2}', f'{year_report}')

            wb_path = write_all_date(f'{year_report}', f'{year_report}')
            files = Files(year=year_report, result_file=wb_path)
            files.save()
            return redirect('success', id=files.id)

        except ValueError:
            messages.success(request, 'Введите корректный год отчета')
            return redirect('upload_files')

    return render(request, 'msfo8/upload_files.html')


def success(request, **kwargs):
    object_id = kwargs.get('id')
    files = Files.objects.get(id=object_id)
    return render(request, 'msfo8/download.html', {'files': files})


def download_file(request, id):
    files = get_object_or_404(Files, id=id)

    if files.result_file:
        with files.result_file.open('rb') as file:
            file_content = file.read()

        content_type = 'application/octet-stream'
        response = HttpResponse(file_content, content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename="result_file.xlsx"'
        return response
    else:
        return HttpResponse('File not found.')


def delete_all_reports(request):
    if request.method == 'POST':
        Files.objects.all().delete()
        directory = 'static/xlsx'
        shutil.rmtree(directory, ignore_errors=True)
        os.makedirs(directory)
        return render(request, 'msfo8/home.html')
    return render(request, 'msfo8/delete_all_reports.html')


def files_list(request):
    files = Files.objects.all()
    return render(request, 'msfo8/files_list.html', {'files': files})


def file_detail(request, id):
    file = get_object_or_404(Files, id=id)

    if request.method == 'POST':
        file.delete()
        messages.success(request, 'Отчет успешно удален.')
        return redirect('files_list')

    return render(request, 'msfo8/file_detail.html', {'file': file})
