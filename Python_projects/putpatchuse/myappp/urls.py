from django.urls import path
from .views import ProductUpdateView

urlpatterns = [
    path('products/<int:pk>', ProductUpdateView.as_view(), name = 'product_update'),
]