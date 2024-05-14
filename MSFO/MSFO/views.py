from django.shortcuts import render


def start_page(request):
    return render(request, 'index.html')


def contacts_page(request):
    return render(request, 'contacts.html')


def instructions_page(request):
    return render(request, 'instructions.html')
