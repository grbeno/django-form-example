from django.urls import path
from .views import HomePageView, StainerpxPageView, CoordsPageView, Form1PageView, Form2PageView, ResultsPageView, getForm, getData, next_data, clear_data

urlpatterns = [ path('', HomePageView.as_view(), name='home'),
				
				path('stainerpx/', StainerpxPageView.as_view(), name='stainerpx'),
				path('coords/', CoordsPageView.as_view(), name='coords'),
				
				path('form/', getForm, name='form'),
				path('results/', getData, name='results'),

				path('next_data', next_data, name='next_data'),
				path('clear_data', clear_data, name='clear_data'),

				path('form1/', Form1PageView.as_view(), name='form1'),
				path('form2/', Form2PageView.as_view(), name='form2'),
				path('results/', ResultsPageView.as_view(), name='results'), ]