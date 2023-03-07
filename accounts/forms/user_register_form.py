from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password','first_name','last_name'] #'username',