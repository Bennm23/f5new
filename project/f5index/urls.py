from django.urls import path

from . import views

app_name='index'
urlpatterns = [
    path('', views.index, name='home'),
    path('contact_support/', views.contact_support, name='contact_support'),
    path('thankyou/', views.thank_you, name='thank_you'),
]

