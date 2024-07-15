from django.urls import path
from core import views

urlpatterns = [
    path("", views.Home, name='Home'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),

    path('signup/', views.Signup, name='Signup'),
    path('login/', views.Login, name='Login'),
]