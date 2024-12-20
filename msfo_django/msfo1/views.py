from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from msfo1.models import ReportFile
from msfo1.tasks import crete_report_task


def msfo1_home(request):
    return render(request, 'msfo1/msfo1_home.html')


def msfo1_generate_report_view(request):
    if request.method == 'POST':
        year_report = request.POST.get('year_report')
        if year_report and year_report.isdigit():
            year_report = int(year_report)
            crete_report_task.delay(year_report)
            messages.success(request, f"The report generation task for {year_report} has been launched.")
            return redirect('msfo1_home')
        else:
            messages.error(request, "Please enter a valid year (number).")
    return render(request, 'msfo1/msfo1_generate_report.html')


def msfo1_report_list(request):
    reports = ReportFile.objects.order_by('-created_at')
    return render(request, 'msfo1/msfo1_report_list.html', {'reports': reports})


def msfo1_report_detail(request, pk):
    report = get_object_or_404(ReportFile, pk=pk)
    if request.method == 'POST':
        # При подтверждении удаления
        messages.success(request, f"Report {report.year_report} deleted successfully.")
        report.delete()
        return redirect('msfo1_report_list')
    return render(request, 'msfo1/msfo1_report_detail.html', {'report': report})
