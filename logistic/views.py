from rest_framework.viewsets import ModelViewSet

from logistic.serializers import ProductPositionSerializer, ProductSerializer, StockSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from logistic.models import Product, Stock, StockProduct



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # при необходимости добавьте параметры фильтрации
    # filter_backends = [SearchFilter]
    # filterset_fields = ['title',]
    search_fields = ['title', 'description',]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    
    filterset_fields = ['products',]
