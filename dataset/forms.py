from cProfile import label
from django  import forms
class upload(forms.Form):
    name = forms.CharField(max_length=250)
    file = forms.FileField()