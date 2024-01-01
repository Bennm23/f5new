from django.urls import path

from . import views

app_name='members'
urlpatterns = [
    path('', views.index, name='home'),
    path('admintools/f5crawler/', views.tools_f5crawler, name='tools_f5crawler'),
    path('admintools/createMember/', views.tools_create_member, name='tools_create_member'),
    path('manage/', views.manage_members, name='manage_members'),
    path('signup/', views.create_member, name='create_member'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_member, name='login_member'),
    path('logout/', views.logout_member, name='logout_member'),
    path('editMember/<int:member_id>', views.edit_member, name='edit_member'),
    path('verifySent/', views.verify_sent, name="verify_sent"),
    path('verify/<str:verification_code>/', views.verify_user, name='verify_user'),
    path('profile/<str:member_username>/', views.public_profile, name='public_profile'),
    path('error/', views.error, name='error')
]
