from django.conf.urls import url
from accounts import views
from django.urls import path

#Template URLS!

# app_name='accounts'

urlpatterns=[
    path('register/', views.register, name='register'),
    path('accounts/login', views.loginPage, name="login"),
    path('accounts/logout', views.logoutUser, name='logout'),
]
