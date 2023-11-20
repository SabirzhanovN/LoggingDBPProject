from django.urls import path

from . import views

urlpatterns = [
    path('logs/', views.LoggingMovesListAPIView.as_view(), name='logs'),
]