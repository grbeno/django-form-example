from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import DemoForm

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
	" Create form in Django "
	
	if request.method == 'POST':
		form = DemoForm(request.POST)	
	else:
		form=DemoForm()
	
	return render(request,'form1.html',{'form': form})

def getData(request):
	" Get data from form "
	
	if request.method == 'POST':
		" It works: "
		#ka = request.POST.get('Ka')
		#humusz = request.POST.get('Humusz')
		" It works too: "
		form = DemoForm(request.POST)
		ka = form['Ka'].value()
		humusz = form['Humusz'].value()
	else:
		return render(request,'form1.html')
	
	context = {'ka':ka,'humusz':humusz, }
	
	return render(request,'results.html',context)
	