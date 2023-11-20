from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete-account/<int:id>', views.delete_account, name='delete_account'),
    path('edit_profile/', views.edit_profile, name='edit_profile')
]