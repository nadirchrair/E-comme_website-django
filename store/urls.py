from django.urls import path
from . import views
urlpatterns = [
    path('product/', views.index, name="index"),
    path('cart/', views.cart, name="cart"),    
    path('cart/delete', views.delete, name="delete"),
    path('product/<str:slug>', views.product_detial, name="product_detial"),
    path('product/<str:slug>/add_to_cart', views.add_cart, name="add_cart"),


]
