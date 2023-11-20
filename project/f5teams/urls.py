from django.urls import path

from . import views

app_name='teams'
urlpatterns = [
    path('', views.index, name='home'),
    # path('create/', views.create, name='create'),
    # path('<int:blog_id>/detail', views.detail, name='detail'),
    # path('<int:blog_id>/edit', views.edit, name='edit'),
    # path('<int:blog_id>/delete', views.delete, name='delete'),

]
