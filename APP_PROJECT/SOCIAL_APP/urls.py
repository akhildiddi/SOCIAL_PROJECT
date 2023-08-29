from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('account/', views.account, name='account'),
    path('submit_activity/', views.submit_activity, name='submit_activity'),
]

