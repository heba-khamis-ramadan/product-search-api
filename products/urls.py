from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductSearchView, home

router = DefaultRouter()
router.register(r'search', ProductSearchView, basename='product-search')

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns.extend(router.urls)
