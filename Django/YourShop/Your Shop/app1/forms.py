from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import delivery

"""
    This file is made for the custom forms used in the website. 
    The class for the form data is used with the Meta class to specify the fields required in the form. 
    Names of the forms are self explainatory. 
"""
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')

class deliveryform(forms.ModelForm):
    
    class Meta:
        model = delivery
        fields = ['name', 'house_no', 'street', 'city', 'pincode']