from django.urls import path

from . import views

app_name='teams'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<int:team_id>/detail', views.detail, name='detail'),
    path('<int:team_id>/edit', views.edit, name='edit'),
    path('<int:team_id>/delete', views.delete, name='delete'),
    path('join/<int:team_id>/', views.join, name='join'),
    path('leave/<int:team_id>/<int:member_id>', views.leave, name='leave'),
    path('match/createMatch/', views.createMatch, name='create_match'),
    path('match/<int:match_id>/detail', views.detailMatch, name='detail_match'),
    path('match/<int:match_id>/submitScoreReport', views.submitScoreReport, name='submit_score_report')


]
