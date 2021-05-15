from django.urls import path
from .views import ProductsAPIView, CategoryAPIView, \
    UniqueProductAPIView, ProductImageAPIView, UniqueCategoryAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view()),
    path('products/<int:id>', UniqueProductAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('products/images/<int:id>', ProductImageAPIView.as_view()),
    path('products/<int:id>/images', ProductImageAPIView.as_view()),
    path('category/<int:id>', UniqueCategoryAPIView.as_view())
]
