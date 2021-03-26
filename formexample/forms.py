from django.forms import ModelForm
from .models import Projectname, Modelform1, Modelform2

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