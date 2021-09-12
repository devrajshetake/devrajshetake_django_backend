from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name = 'login'),
    path('user-home/', views.home, name = 'home'),
    path('logout/', views.logout, name = 'logout'),
    path('search/', views.search, name = 'search'),

]