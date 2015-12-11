from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		widgets = {
		'name':forms.TextInput(attrs = {'placeholder': 'Your Name*'}),
		'email':forms.TextInput(attrs = {'placeholder': 'Contact e-mail*'}),
		'phone':forms.TextInput(attrs = {'placeholder': 'Contact Phone*'}),
		'location':forms.TextInput(attrs = {'placeholder': 'City*'}),
		'details':forms.TextInput(attrs = {'placeholder': 'Event Details (Optional)'}),


		}