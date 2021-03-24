from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import DemoForm_1, DemoForm_2, DemoForm_3
from .models import Projectname, Modelform1

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
		project = form1['project'].value()
		form1.save()
		#project = Projectname.objects.all()

		form2 = DemoForm_2(request.POST)
		ph = form2['ph'].value()
		thk = form2['thk'].value()
		ka = form2['ka'].value()
		humusz = form2['humusz'].value()
		form2.save()
		#params1 = Modelform1.objects.all()
		params1 = [ph,thk,ka,humusz]

		form3 = DemoForm_3(request.POST)
		p2o5 = form3['p2o5'].value()
		k2o = form3['k2o'].value()
		form3.save()
		params2 = [p2o5,k2o] 
		
		context = {'project': project, 'params1': params1, 'params2': params2, }
		
	else:
		form1 = DemoForm_1()
		form2 = DemoForm_2()
		form3 = DemoForm_3()
		return redirect('/form/')
	
	return render(request,'results.html',context)



	