from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListViews.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailViews.as_view(), name='product') # llave primaria o ID
    
]
