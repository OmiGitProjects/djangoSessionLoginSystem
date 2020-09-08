from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.instructorRegister, name='register'),
    path('login/', views.instructor_login, name='login'),
    path('homepage/', views.homepage, name='home-page'),
    path('logout/', views.logout, name='logout'),
]