from django.urls import path
from . import views
from users.views import home

urlpatterns = [
    path("", home, name="home"),
    path("", views.user, name="user"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]