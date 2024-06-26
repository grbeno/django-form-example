from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import DemoForm_1, DemoForm_2, DemoForm_3
from .models import Projectname, Modelform1, Modelform2, StainerModel
from django.template.loader import render_to_string

#from django.views.decorators.csrf import csrf_exempt
#from django.http import JsonResponse
#from django.views.decorators.http import require_POST
import os
from .stainerpx import mkmask, stainer

" Some template views "

# Home

class HomePageView(TemplateView):
	template_name = 'home.html'

# StainerPx

class StainerpxPageView(TemplateView):
	template_name = 'stainerpx.html'

class CoordsPageView(TemplateView):
	template_name = 'coords.html'

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
		
		print(list(param1.values('ph','thk','ka','humusz'))) # list of dictionaries
		
	else:

		form1 = DemoForm_1()
		form2 = DemoForm_2()
		form3 = DemoForm_3()
		
		return redirect('/form/')
	
	return render(request,'results.html',context)

""" 
def getImage(request):
	" ... "
	return render(request,'results.html',context)
"""

#@csrf_exempt
#@require_POST
def passCoords(request):
	
	MINIMUM_POINTS = 3
	context = {}
	img_path = 'static//images//' 
	st_data = []
	
	if request.method == 'POST': # request.is_ajax() and 
				
		coords = request.POST.getlist('coords[]')
		colors = int(request.POST.get('colors'))
		
		if len(coords) >= MINIMUM_POINTS:
			
			" Mask image "
			mkmask(coords,img_path)
			
			" Stainer "
			st_data = stainer(colors,img_path)
			
			" Context to Model "
			StainerModel.objects.all().delete()
			StainerModel.objects.create(coords=coords,st_colors=st_data)

	#else:
		#return HttpResponse(' Empty context! Add coordinates with mouse click! ') # GET request
		#return render(request, 'coords.html', context)

	st_query = StainerModel.objects.all()
	context = {'st_query': st_query}
	
	return render(request, 'coords.html', context)


def delete_coords(request):
	try:
		# Delete data (coords,color%)
		StainerModel.objects.all().delete()
		# Delete images
		os.remove('static//images//prepared.png')
		os.remove('static//images//stain.png')
		os.remove('static//images//pie_st.png')
	except:
		pass
	
	return redirect('/stainerpx/')

def clear_data(request):
	Projectname.objects.all().delete()
	Modelform1.objects.all().delete()
	Modelform2.objects.all().delete()
	return redirect('/form/')

def next_data(request):
	return redirect('/form/')


	