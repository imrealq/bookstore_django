from django.forms import ModelForm

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