from django.urls import path
from profiles_api import views


urlPartterns = [
    path('hello-world/', views.HelloApiView.as_view()),
]