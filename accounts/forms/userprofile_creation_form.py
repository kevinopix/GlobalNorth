from accounts.models import UserProfile
from django import forms


class UserProfileCreationForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['location','is_active','terms_conditions_accepted','phone_number']
		# 'report_number': forms.CharField(attrs={'class': 'form-control'})
		widgets = {
			'location': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "Enter your Location"}
			),
			'terms_conditions_accepted': forms.CheckboxInput(
				attrs={'class': 'required checkbox'}
			)
		}
		labels = {
			'terms_conditions_accepted': 'By checking the box above, I agree to the terms & conditions of this contract'
		}