from django.urls import path
from .views import home, login, signup, profile, search_detail, search_detail_t,logout

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("search-detail/<slug:slug>/<int:id>/", search_detail, name="search_detail"),
    path("search-detail/", search_detail_t, name="search_detail_t"),
    path("logout/", logout, name="logout"),
]