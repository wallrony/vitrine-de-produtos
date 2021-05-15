from rest_framework import serializers

from .models import Product, ProductCategory, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description',
                  'price', 'category', 'created_at', 'updated_at')

    def is_valid(self, raise_exception=False):
        print(self.data.get('name'))

        return True


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id', 'name', 'created_at', 'updated_at'
        )


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = (
            'id', 'image', 'created_at', 'updated_at'
        )
