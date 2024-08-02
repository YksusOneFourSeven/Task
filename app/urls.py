from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ParameterListView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('parameters/', ParameterListView.as_view(), name='parameter-list'),
]
