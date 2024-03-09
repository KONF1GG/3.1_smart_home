from django.urls import path

from .views import API, APIputch, APIMesurments

urlpatterns = [
    path('sensors/', API.as_view()),
    path('sensors/<pk>/', APIputch.as_view()),
    path('measurements/', APIMesurments.as_view()),
]
