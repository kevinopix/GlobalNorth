from accounts.models import UserProfile
from django import forms


class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['location',]
		widgets = {
			'location': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "Update your Location"}
			)
		}