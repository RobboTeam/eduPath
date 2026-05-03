from django import forms
from .models import Material

class FeedbackForm(forms.ModelForm): 
  class Meta:
    model = Material
    fields = ("subject", "title")

class UserReg(forms.Form):
  username = forms.CharField(max_length=150, required=True)
  password = forms.CharField(max_length=16, required=True, widget=forms.PasswordInput())
  first_name = forms.CharField(max_length=150, required=False)
  last_name = forms.CharField(max_length=150, required=False)
  email = forms.EmailField(required=False)
  
class UserAuthentication(forms.Form):
  username = forms.CharField(required=True)
  password = forms.CharField(required=True, widget=forms.PasswordInput)