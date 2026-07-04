from django.contrib import admin
from django.urls import path
from library.views import landing_view, checkout_view, payment_view
from users.views import register_view, profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='landing'),
    path('checkout/', checkout_view, name='checkout'),
    path('payment/<int:order_id>/', payment_view, name='payment'),
    
    # Авторизация
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='landing'), name='logout'),
    path('accounts/register/', register_view, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
]