from os import replace

from django.shortcuts import render, redirect
from .models import Files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from msfo8.tasks import crete_report_task


def home(request):
    return render(request, 'msfo8/report1002.html')


def upload_files(request):
    if request.method == 'POST':

        try:

            year_report = int(request.POST.get('year_report'))
            if 1980 > year_report or 2100 < year_report:
                raise ValueError

            crete_report_task.delay(year_report)

            return render(request, 'msfo8/success.html')

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
    file_name = str(files.result_file).replace('/code/MSFO/static/xlsx/', '')

    if files.result_file:
        with files.result_file.open('rb') as file:
            file_content = file.read()

        content_type = 'application/octet-stream'
        response = HttpResponse(file_content, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    else:
        return HttpResponse('File not found.')


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
