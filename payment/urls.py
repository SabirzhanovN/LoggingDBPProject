from django.urls import path

from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('replenish/', views.replenish_verdict, name='replenish_verdict'),
]