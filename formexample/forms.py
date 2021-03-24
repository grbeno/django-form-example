from django.forms import ModelForm
from .models import Projectname, Modelform1, Modelform2
"""
from django import forms 

class DemoForm_1(forms.Form):
	Ka = forms.CharField(max_length=20, label='KA') 
	Humusz = forms.CharField(max_length=20, label='H%')

class DemoForm_2(forms.Form):
	Ph = forms.CharField(max_length=20, label='PH') 
	Thk = forms.CharField(max_length=20, label='Thk')

class DemoForm_3(forms.Form):
	P2o5 = forms.CharField(max_length=20, label='P2O5') 
	K2o = forms.CharField(max_length=20, label='K2O')
"""

class DemoForm_1(ModelForm):
    class Meta:
        model = Projectname
        fields = '__all__'

class DemoForm_2(ModelForm):
    class Meta:
        model = Modelform1
        fields = '__all__'

class DemoForm_3(ModelForm):
    class Meta:
        model = Modelform2
        fields = '__all__'