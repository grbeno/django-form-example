from django import forms 

class DemoForm(forms.Form):
	Ka = forms.CharField(max_length=20, label='KA') 
	Humusz = forms.CharField(max_length=20, label='H%')