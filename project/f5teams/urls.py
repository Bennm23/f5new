from django.urls import path

from . import views

app_name='teams'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<int:team_id>/detail', views.detail, name='detail'),
    path('<int:team_id>/edit', views.edit, name='edit'),
    path('<int:team_id>/delete', views.delete, name='delete'),
    path('<int:team_id>/join/<int:member_id>', views.join, name='join'),
    path('<int:team_id>/leave/<int:member_id>', views.leave, name='leave'),


]
