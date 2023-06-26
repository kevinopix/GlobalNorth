from accounts.models import UserProfile
from django import forms


class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['location','phone_number']
		widgets = {
			'location': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "Update your Location"}
			),
			'phone_number': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "Update your Phone Number"}
			)
		}