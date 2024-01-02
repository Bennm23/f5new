from django.urls import path

from . import views


app_name='store'
urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create_product'),
    path('product/<str:product_id>/detail', views.detail, name='product_detail'),
    path('<int:product_id>/edit', views.edit, name='product_edit'),
    path('<int:product_id>/delete', views.edit, name='product_delete'),
    path('checkout', views.initiate_checkout, name="checkout"),
    path('checkout_error/', views.checkout_error, name="checkout_error"),
    path('checkout_success/', views.checkout_success, name="checkout_success"),
]
