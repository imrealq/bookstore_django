from django.http import HttpResponse

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

def unauthenticated_user(view_func):

	def wrapper_func(request, *arg, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *arg, **kwargs)
	
	return wrapper_func