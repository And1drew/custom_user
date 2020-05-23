from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from my_user.models import My_User
from my_user.forms import Login_Form
# Create your views here.


@login_required
def index(request):
    user_info = My_User.objects.all()
    return render(request, 'index.html', {'user_info': user_info})


# def add_user_view(request):

"""
def login_view(request):
    if request.method == "POST":
        form = Login_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, user_name=data['user_name'], password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('/')
    form = Login_Form()
    return render(request, 'login_view.html', {'form': form})
"""


def login_view(request):
    form = Login_Form(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(
            request, user_name=data['user_name'], password=data['password']
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    form = Login_Form()
    return render(request, 'login_view.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('loginpage'))
