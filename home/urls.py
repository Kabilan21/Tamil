from django.urls import path

from . import views

urlpatterns = [
    path('', views.html_view, name='home')
]
