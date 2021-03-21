from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import DemoForm_1, DemoForm_2, DemoForm_3

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
		ka = form1['Ka'].value()
		humusz = form1['Humusz'].value()

		form2 = DemoForm_2(request.POST)
		ph = form2['Ph'].value()
		thk = form2['Thk'].value()

		form3 = DemoForm_3(request.POST)
		p2o5 = form3['P2o5'].value()
		k2o = form3['K2o'].value()
		
		context = {'ka':ka,'humusz':humusz,'ph':ph,'thk':thk, 'p2o5':p2o5,'k2o':k2o, }
	else:
		form1 = DemoForm_1()
		form2 = DemoForm_2()
		form3 = DemoForm_3()
		return redirect('/form/')
	
	return render(request,'results.html',context)




""" def getForm_1(request):
	" Create form in Django "
	if request.method == 'POST':
		form1 = DemoForm_1(request.POST)
	else:
		form1 = DemoForm_1()
	return render(request,'form1.html',{'form': form1})

def getForm_2(request):
	" Create form in Django "
	if request.method == 'POST':
		form2 = DemoForm_2(request.POST)
	else:
		form2 = DemoForm_2()
	return render(request,'form1.html',{'form': form2}) """



""" def getData_1(request):
	" Get data from form "
	context = {}
	if request.method == 'POST':
		" It works too: "
		form = DemoForm_1(request.POST)
		ka = form['Ka'].value()
		humusz = form['Humusz'].value()
		context = {'ka':ka,'humusz':humusz, }
	else:
		form = DemoForm_1()
		return redirect('/form1/')
	return render(request,'results.html',context)

def getData_2(request):
	" Get data from form "
	context = {}
	if request.method == 'POST':
		" It works too: "
		form = DemoForm_2(request.POST)
		ph = form['Ph'].value()
		thk = form['Thk'].value()
		context = {'ph':ph,'thk':thk, }
	else:
		form = DemoForm_2()
		return redirect('/form2/')
	return render(request,'results.html',context) """

	