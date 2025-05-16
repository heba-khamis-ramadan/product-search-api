from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductSearchView

router = DefaultRouter()
router.register(r'search', ProductSearchView, basename='product-search')

urlpatterns = router.urls
