from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import User


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','first_name','last_name', 'password1', 'password2',)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','first_name','last_name')