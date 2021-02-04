from django.urls import path, include
from .views import GenericAPIView, BookAPIView, BookViewSet, BookDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('viewset', include(router.urls)),
    path('generic/book/<int:id>/', GenericAPIView.as_view()),
    path('detail/<int:id>/', BookDetails.as_view()),
    path('book/', BookAPIView.as_view()),
]
