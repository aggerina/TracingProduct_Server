from django.forms import  ModelForm
from django import  forms
from INV.models import Part

class PartForm(ModelForm):
    class Meta:
        model = Part
        fields  = [ 'name', 'PartNumber', 'description', 'image', 'price','slug', 'Quantiti' ]




class AdminForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Part.objects.all())
    question = forms.CharField(widget=forms.Textarea)
    q_active = forms.BooleanField(initial=True)
    option = forms.CharField()
    option_active = forms.BooleanField(initial=True)
