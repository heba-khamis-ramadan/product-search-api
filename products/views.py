from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_TERMS

from .documents import ProductDocument
from .serializers import ProductSearchSerializer
from django.shortcuts import render

def home(request):
    print("Home view called!")
    return render(request, 'products/index.html')

class CustomPagination(PageNumberPagination):
    page_size = 10         # Number of results per page
    page_size_query_param = 'page_size'  # Allow client to override page size with ?page_size=XX
    max_page_size = 100

class ProductSearchView(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSearchSerializer
    pagination_class = CustomPagination

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend,
    ]

    search_fields = {
        'name': {'boost': 5, 'fuzziness': 'AUTO'},
        'brand': {'boost': 3, 'fuzziness': 'AUTO'},
        'category': {'boost': 2},
        'nutrition_facts': {'boost': 1}
    }

    filter_fields = {
        'price': 'price',
        'category': 'category',
        'brand': 'brand',
    }

    ordering_fields = {
        'price': 'price',
        'name': 'name',
    }

    ordering = ('price',)
