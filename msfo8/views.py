from django.shortcuts import render, redirect
from .models import Files, Material, Store
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from msfo8.excel.utils import write_all_date_bd
from msfo8.excel.excel_write import write_all_date
import shutil
import os


def home(request):
    return render(request, 'msfo8/home.html')


def upload_files(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        file1 = request.FILES.get('file1')
        file2 = request.FILES.get('file2')

        files = Files(name=name, file1=file1, file2=file2)
        files.save()

        return redirect('success', id=files.id)

    return render(request, 'msfo8/upload_files.html')


def success(request, **kwargs):
    object_id = kwargs.get('id')
    files = Files.objects.get(id=object_id)
    path1 = files.file1
    path2 = files.file2
    Material.objects.all().delete()
    Store.objects.all().delete()
    write_all_date_bd(f'{path1}', '2023')
    write_all_date_bd(f'{path2}', '2023')
    wb_path = write_all_date('2023', '2023')
    files.result_file = wb_path
    files.save()
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
        return redirect('home')
    return render(request, 'msfo8/delete_all_reports.html')
