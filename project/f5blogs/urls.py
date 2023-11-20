from django.urls import path

from . import views

app_name='blogs'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>', views.delete, name='delete'),

]

