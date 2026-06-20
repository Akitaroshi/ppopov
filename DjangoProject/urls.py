from django.contrib import admin
from django.urls import path
from library.views import landing_view, about_view
from users.views import register_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about_view, name='about'),                     # Главная страница: О нас
    path('catalog/', landing_view, name='landing'),         # Страница каталога: /catalog/
    
    # Авторизация и профиль
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='about'), name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
]