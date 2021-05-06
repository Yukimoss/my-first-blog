from django.urls import path

from . import views

urlpatterns = [
    path('machine_learning', views.file_upload, name='machine_learning'),
    ]