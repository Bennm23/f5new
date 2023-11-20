from django.urls import path

from . import views

app_name='blogs'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
]

