from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('binary_compare/', views.binary_compare, name='binary_compare'),
    path('vulnerability_analysis/', views.vulnerability_analysis, name='vulnerability_analysis'),
] 