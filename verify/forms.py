
from django import forms 
  
# creating a form  
class InputForm(forms.Form): 
  
    phone = forms.IntegerField()

