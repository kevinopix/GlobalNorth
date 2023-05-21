from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter your Email"}
    ))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter your First Name"}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter your Last Name"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': "Enter your Password"}
    ))

    class Meta:
        model = User
        fields = ['email', 'password','first_name','last_name'] #'username',