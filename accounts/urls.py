from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_page, name="login"),
    path("register", views.register_page, name="register"),
    path("logout", views.logout_page, name="logout"),

    path("dashboard", views.dashboard_page, name="dashboard"),


]