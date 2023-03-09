from accounts.models import UserProfile
from django import forms


class UserProfileCreationForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['location',]
		# 'report_number': forms.CharField(attrs={'class': 'form-control'})
		widgets = {
			'location': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "Enter your Location"}
			)
		}