from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_TERMS, LOOKUP_QUERY_FUZZY

from .documents import ProductDocument
from .serializers import ProductSearchSerializer

class ProductSearchView(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSearchSerializer
    pagination_class = PageNumberPagination

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend,
    ]

    search_fields = {
        'name': {'boost': 5, 'options': {'fuzziness': 'AUTO'}},
        'brand': {'boost': 3, 'options': {'fuzziness': 'AUTO'}},
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
