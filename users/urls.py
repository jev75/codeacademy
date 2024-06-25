from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('facebook_login/', views.facebook_login, name='facebook_login'),
    path('google_login/', views.google_login, name='google_login'),

]