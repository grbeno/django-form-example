from django.urls import path
from .views import HomePageView, Form1PageView, Form2PageView, ResultsPageView, getForm, getData

urlpatterns = [ path('', HomePageView.as_view(), name='home'),
				
				path('form/', getForm, name='form'),
				path('results/', getData, name='results'),

				path('form1/', Form1PageView.as_view(), name='form1'),
				path('form2/', Form2PageView.as_view(), name='form2'),
				path('results/', ResultsPageView.as_view(), name='results'),]