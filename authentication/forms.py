from django.forms import ModelForm, TextInput, EmailInput,  PasswordInput, DateInput, Select, NumberInput, Textarea

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms 

from .models import BooksInfo

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CreateBook(ModelForm):
	class Meta:
		model = BooksInfo
		fields = '__all__'

		widgets = {
			'book_title': TextInput(attrs={
				'class': "form-control",
	        	'placeholder': 'Book title',
				}),
			'release_date': DateInput(attrs={
			    'class': "form-control",
			    'type': 'date',
				}),
			'author': Select(attrs={
				'class': "form-control",
				}),
			'price': NumberInput(attrs={
				'class': "form-control",
				'placeholder': '0'
				}),
			'short_description': Textarea(attrs={
				'class': "form-control",
				'placeholder': 'Short description about the book'
				}),	
		}