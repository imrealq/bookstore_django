from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.

from .forms import CreateUserForm, CreateBook

from .decorators import unauthenticated_user, login_required

from .models import BooksInfo

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

			user = form.cleaned_data['username']
			messages.success(request, f'Account {user} was created')

			return redirect('login')	
	
	context = {'form': form}

	return render(request,'authentication/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or Password is incorrect')

	context = {'logined': False}
	return render(request, 'authentication/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	books = BooksInfo.objects.all()

	context = {'books': books, 'logined': True}
	return render(request, 'authentication/home.html', context)

@login_required(login_url='login')
def createBook(request):
	form = CreateBook(auto_id="id_%s")
	if request.method == "POST":
		form = CreateBook(request.POST)
		if form.is_valid():
			form.save()
			book = form.cleaned_data['book_title']
			messages.success(request, f'Book "{book}" was added')
			return redirect('home')

	context = {'form': form}
	return render(request, 'authentication/create_book.html', context)

@login_required(login_url='login')
def updateBook(request, pk):
	book = BooksInfo.objects.get(id=pk)
	form = CreateBook(instance=book)

	if request.method == "POST":
		form = CreateBook(request.POST, instance=book)
		if form.is_valid():
			form.save()
			book = form.cleaned_data['book_title']
			messages.success(request, f'Book "{book}" was updated')
			return redirect('home')


	context = {'form':form}
	return render(request, 'authentication/update_book.html', context)

@login_required(login_url='login')
def deleteBook(request, pk):
	book = BooksInfo.objects.get(id=pk)
	
	if request.method == "POST":
		book.delete()
		messages.success(request, f'Book "{book.book_title}" was deleted')
		return redirect('home')

	context = {'book': book}
	return render(request, 'authentication/delete_book.html', context)