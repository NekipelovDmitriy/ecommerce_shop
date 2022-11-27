from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/<str:id>/', views.product, name='product'),

    path('update-item/', views.updateItem, name='update-item'),
]