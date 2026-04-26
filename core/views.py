from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")

@login_required
def profile(request):
    return render(request, "profile.html")

@login_required
def search_detail(request):
    return render(request, "search_detail.html")

@login_required
def search_detail_t(request):
    return render(request, "search_detail.html")


@login_required
def logout(request):
    return redirect("core:login")