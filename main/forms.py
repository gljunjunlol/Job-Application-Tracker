from django import forms

from .models import Contact

class CreateNewList(forms.Form): # form name and inherit from forms.Form
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)



class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'purpose', 'role', 'location', 'date', 'message']

		widgets = {
			'name' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
			# email can put EmailInput
			'email' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'you@email.com'}),
			'role' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'position'}),
			'location' : forms.TextInput(attrs={'class': 'input', 'placeholder': 'work location'}),
			'date' : forms.DateInput(attrs={'class': 'input', 'placeholder': 'dd/mm/yyyy'}),
			'message' : forms.Textarea(attrs={'class': 'textarea', 'rows': 10, 'placeholder' : 'Your message...'}),

		}