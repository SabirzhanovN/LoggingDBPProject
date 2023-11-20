from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('detail/<int:id>/', views.detail, name='detail'),
]