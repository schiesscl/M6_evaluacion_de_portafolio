from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'auth_p6'

urlpatterns = [
    # Login y Logout
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Registro
    path('register/', views.register_view, name='register'),
    
    # Perfil
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]