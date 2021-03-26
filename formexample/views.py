from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import DemoForm_1, DemoForm_2, DemoForm_3
from .models import Projectname, Modelform1, Modelform2

" Some template views "

# Home

class HomePageView(TemplateView):
	template_name = 'home.html'

# Form_1

class Form1PageView(TemplateView):
	template_name = 'form1.html'

# Form_2

class Form2PageView(TemplateView):
	template_name = 'form2.html'

# Results

class ResultsPageView(TemplateView):
	template_name = 'results.html'


# Forms

def getForm(request):
	if request.method == 'POST':
		form1 = DemoForm_1(request.POST)
		form2 = DemoForm_2(request.POST)
		form3 = DemoForm_3(request.POST)
	else:
		form1 = DemoForm_1()
		form2 = DemoForm_2()
		form3 = DemoForm_3()
	return render(request,'form.html',{'form1': form1, 'form2': form2, 'form3': form3})

def getData(request):
	" Get data from form "
	
	context = {}
	
	if request.method == 'POST':

		form1 = DemoForm_1(request.POST)
		form1.save()
		project = Projectname.objects.all() # QuerySet
		
		form2 = DemoForm_2(request.POST)
		form2.save()
		param1 = Modelform1.objects.all()
		
		form3 = DemoForm_3(request.POST)
		form3.save()
		param2 = Modelform2.objects.all()
		
		context['group'] = zip(project,param1,param2)
		
	else:
		
		form1 = DemoForm_1()
		form2 = DemoForm_2()
		form3 = DemoForm_3()
		
		return redirect('/form/')
	
	return render(request,'results.html',context)

def clear_data(request):
	Projectname.objects.all().delete()
	Modelform1.objects.all().delete()
	Modelform2.objects.all().delete()
	return redirect('/form/')

def next_data(request):
	return redirect('/form/')


	