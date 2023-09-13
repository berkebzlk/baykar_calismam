from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterUserView.as_view(), name="register-user"),
    path("login/", views.LoginUserView.as_view(), name="login-user"),
    path("logout/", views.logout_user_view, name="logout-user"),
]
