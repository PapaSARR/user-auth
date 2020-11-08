from user.forms import UserForm
from django.http import HttpResponseRedirect
from user.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

def connexion(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
        	email = form.cleaned_data['email']
        	password = make_password(form.cleaned_data['password'])
 
	       	User.objects.create(email=email,password=password)
        	return redirect('/view')	        
    else:
        form = UserForm() 
    return render(request, 'index.html', {'form': form}) 