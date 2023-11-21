from django.urls import path

from . import views


app_name='store'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='product_create'),
    path('<int:product_id>/detail', views.detail, name='product_detail'),
    path('<int:product_id>/edit', views.edit, name='product_edit'),
    path('<int:product_id>/delete', views.edit, name='product_delete'),
]
