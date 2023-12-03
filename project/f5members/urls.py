from django.urls import path

from . import views

app_name='members'
urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.create_member, name='create_member'),
    path('dashboard/<str:member_username>/', views.dashboard, name='dashboard'),
    path('login/', views.login_member, name='login_member'),
    path('logout/', views.logout_member, name='logout_member'),
    path('editMember/', views.edit_member, name='edit_member'),
    path('verifySent/', views.verify_sent, name="verify_sent"),
    path('verify/<str:verification_code>/', views.verify_user, name='verify_user'),
]
