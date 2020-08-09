from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.HomepageView.as_view(), name='home'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logged/out/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
]