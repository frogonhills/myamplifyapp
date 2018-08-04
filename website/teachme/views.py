from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def index(request):
	return render(request, 'index.html')
def post(request):
	return HttpResponse("<h1> this is post </h1>")


def signin(request):
	
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = form.get_user()
			login(request, user)
			return redirect('index')        
	else:
		form = AuthenticationForm()
	return render(request, 'signin.html', {'form': form})
	
	
	
	
	
	

	
	
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})





def profile(request):
	return HttpResponse("<h1> this is profile </h1>")
	
	
	

