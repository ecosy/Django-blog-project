from django import forms
from django.core.exceptions import ValidationError
from .models import User

# class LoginForm(forms.Form):
#     user_id = forms.CharField(max_length=10, help_text="your id")
#     user_pwd = forms.CharField(max_length=20, help_text="your password")
#
#     def clean_user_id(self):
#         data = self.cleaned_data['user_id']
#         return data
#
#     def clean_user_pwd(self):
#         data = self.cleaned_data['user_pwd']
#         return data

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'name', 'description']
