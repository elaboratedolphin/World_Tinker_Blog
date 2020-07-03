from django.shortcuts import render, redirect
from accounts.forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

############https://www.geeksforgeeks.org/django-sign-up-and-login-with-confirmation-email-python/#########
def index(request):
    return render(request, 'posts/post_detail.html')

########### register here #####################################
def register(request):
    register_form = CreateUserForm()
    registered = False
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()
            # user.set_password(user.password)
            group = Group.objects.get(name='Members')
            group.save()
            user.groups.add(group)
            user.save()
            user = register_form.cleaned_data.get('username')
            messages.success(request, "Successfully registered! " + user)
            registered = True
        else:
            print(register_form.errors)

    else:
        register_form = CreateUserForm()

    return render(request, 'registration/registration.html', {'register_form':register_form,
                                                             'registered': registered})

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome back " + username + "!")
            return redirect('post_list')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return redirect('post_list')

def logoutUser(request):
	logout(request)
	return redirect('post_list')
