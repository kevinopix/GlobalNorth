from django.contrib.auth import authenticate
from django import forms


class UserLoginForm(forms.Form):
    email = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            # returns user objects if credentials are correct
            user = authenticate(email=email, password=password)

            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)