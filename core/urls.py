from django.urls import path
from .views import home, login, signup, profile, search_detail,logout

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("search-detail/<slug:slug>/<int:id>/", search_detail, name="search_detail"),
    path("logout/", logout, name="logout"),
]