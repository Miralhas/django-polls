from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_poll/<int:number_options>", views.add_poll, name="add_poll"),
    path("poll_page<int:poll_pk>", views.poll_page, name="poll_page"),

    # Login / Register Views
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
] 