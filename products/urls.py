from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('productDetails/', views.showDetails),
    path('search/', views.search, name="search"),
    path('cart/', include('Cart.urls')),
    path('<str:category_sent>/<str:type>/', views.showByCategory)
]