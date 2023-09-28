from django.shortcuts import render, redirect
from machine.models import Report, Machine
from accounts.models import CustomUser
from machine.forms import ReportForm

def home(request):
    context = {
        'machines': Machine.objects.all(),
		'reports': Report.objects.all()
	}
    return render(request, 'machine/home.html', context=context)

def report(request, pk):
    context = {
		'report': Report.objects.get(pk=pk)
	}
    return render(request, 'machine/report.html', context=context)

from django.contrib import messages
def report_create(request):
	if request.method == "POST":
		form = ReportForm(request.POST)
		if form.is_valid():
			instance = form.save()
			messages.success(request, "Your machine has been successfully added!")
			return redirect("home")
		else:
			messages.error(request, "Please correct the error below")
	else:
		form = ReportForm()
	context = {"form" : form}
	return render(request, 'machine/report_create.html', context = context)
# Create your views here.
