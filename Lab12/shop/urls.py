from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/add/', views.add_category, name='add_category'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/<int:pk>/review/add/', views.add_review, name='add_review'),
]