from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import SignupForm, LoginForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from agent import search as get_search 
from .models import Search, Tag

User = get_user_model()

def home(request):
    data = None
    message = request.GET.get("search")
    
    if message:
        data = get_search(message)
        
        tag, _ = Tag.objects.get_or_create(name=data["tag"])
        
        Search.objects.create(
            user=request.user,
            tag=tag,
            query=message,
            what_is=data["what_is"],
            how_it_works=data["how_it_works"],
            code_example=data["code_example"],
            when_to_use=data["when_to_use"],
        )

    return render(request, "home.html", {"data": data})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(username=username, email=email, password=password)
            return redirect("core:login")
    else:
        form = SignupForm()
    
    return render(request, "signup.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                django_login(request, user)
                return redirect("core:home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form":form})

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
    django_logout(request)
    return redirect("core:login")