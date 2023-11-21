from django.urls import path

from . import views


app_name='store'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('<int:product_id>/detail', views.detail, name='detail'),
    path('<int:product_id>/edit', views.edit, name='edit'),
    path('<int:product_id>/delete', views.edit, name='delete'),

]
