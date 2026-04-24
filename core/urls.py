from django.urls import path
from .views import home, login, signup, profile, logout

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout, name="logout"),
]