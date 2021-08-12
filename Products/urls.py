from django.urls import path
from . import views

urlpatterns = [
    path('addproduct/', views.AddProduct, name = 'addproduct'),
    path('showproduct/', views.ShowProduct, name = 'showproduct'),
    
]