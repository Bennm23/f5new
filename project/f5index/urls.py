from django.urls import path

from . import views

app_name='index'
urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.create_member, name='create_member'),
    path('login/', views.login_member, name='login_member'),
]

