from django.shortcuts import render, redirect
from .models import Files, Material, Store
from msfo8.excel.utils import write_all_date_bd
from msfo8.excel.excel_write import write_all_date


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

    return render(request, 'msfo8/upload_file.html')


def success(request, **kwargs):
    object_id = kwargs.get('id')
    files = Files.objects.get(id=object_id)
    path1 = files.file1
    path2 = files.file2
    Material.objects.all().delete()
    Store.objects.all().delete()
    write_all_date_bd(f'{path1}', '2023')
    write_all_date_bd(f'{path2}', '2023')
    write_all_date('2023', '2023')
    files.result_file = '/home/foile/MSFO/MSFO/static/xlsx/data.xlsx'
    files.save()
    return render(request, 'msfo8/success.html', {'files': files})
