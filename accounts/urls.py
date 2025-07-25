from django.contrib.auth import views as auth_views
from .views import register_view
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
    path('signup/', register_view, name='signup'),
]
