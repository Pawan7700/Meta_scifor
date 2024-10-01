
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

