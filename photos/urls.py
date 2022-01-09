from django.urls import path
from . import views

urlpatterns = [
    path('gallery', views.gallery, name="gallery"),
    path('photo/<str:pk>/', views.viewphoto, name="view"),
    path('add/', views.addphoto, name="add"),
]
