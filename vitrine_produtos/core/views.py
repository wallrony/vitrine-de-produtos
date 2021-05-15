import os

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import View
from django.shortcuts import render

from .permissions import UserHavePermission
from .models import Product, ProductCategory, ProductImage
from .serializers import ProductSerializer, ProductCategorySerializer, \
    ProductImageSerializer
from .utils import get_req_url

from vitrine_produtos.validation_messages import field_is_missing, \
    create_message, image_upload_error


class ProductsAPIView(GenericAPIView):
    permission_classes = [UserHavePermission]

    def get(self, request):
        data = get_product_list(request)

        return Response(data)

    def post(self, request):
        err = self.validate_product(request.data)

        if err is not None:
            return Response(
                err,
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            category = ProductCategory.objects.get(
                id=request.data.get('category')
            )
        except ProductCategory.DoesNotExist:
            return Response(
                create_message('A categoria inserida não existe.'),
                status=status.HTTP_400_BAD_REQUEST
            )

        product = Product.objects.create(
            name=request.data.get('name'),
            price=request.data.get('price'),
            description=request.data.get('description'),
            category=category,
        )

        if product is not None:

            file_keys = request.FILES.keys()

            for key in file_keys:
                result = self.upload_image(product.id, request.FILES[key])

                if not result:
                    return Response(
                        image_upload_error(),
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR
                    )

            serializer = ProductSerializer(product)

            data = serializer.data
            data['images'] = get_product_images(product.id, get_req_url(request))

            return Response(
                data,
                status=status.HTTP_201_CREATED
            )

        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def validate_product(self, data):
        name = data.get('name')
        price = data.get('price')
        categories = data.get('category')

        if name is None:
            return field_is_missing('name')
        elif price is None:
            return field_is_missing('price')
        elif categories is None:
            return field_is_missing('categories')

        return None

    def upload_image(self, product_id, image):
        image = ProductImage.objects.create(product_id=product_id, image=image)

        if image is not None:
            return True
        return False


class UniqueProductAPIView(GenericAPIView):
    permission_classes = [UserHavePermission]

    def put(self, request, id):
        product = Product.objects.filter(pk=id).update(
            name=request.data.get('name'),
            description=request.data.get('description'),
            price=request.data.get('price'),
            category_id=request.data.get('category')
        )

        if product > 0:
            return Response(None)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = Product.objects.get(pk=id)
        images = ProductImage.objects.filter(product_id=id)

        for img in images:
            try:
                os.remove(img.image.path)
            except:
                pass
            img.delete()

        product.delete()

        return Response()


class ProductImageAPIView(GenericAPIView):
    permission_classes = [UserHavePermission]

    # id -> product id
    def post(self, request, id):
        for key in request.FILES.keys():
            img = ProductImage.objects.create(product_id=id, image=request.FILES[key])

        return Response(None, status=status.HTTP_201_CREATED)

    # id -> image id
    def delete(self, request, id):
        try:
            image = ProductImage.objects.get(pk=id)
        except ProductImage.DoesNotExist:
            return Response({
                'message': 'category not found'
            }, status=status.HTTP_400_BAD_REQUEST)

        image.delete()

        return Response(None)


class CategoryAPIView(GenericAPIView):
    permission_classes = [UserHavePermission]

    def get(self, request):
        categories = ProductCategory.objects.all()

        serializer = ProductCategorySerializer(categories, many=True)

        ordered_list = sorted(serializer.data, key=lambda k: k['id'])

        return Response(ordered_list)

    def post(self, request):
        name = request.data.get('name')

        if name is None:
            return Response(
                field_is_missing('name'),
                status=status.HTTP_400_BAD_REQUEST
            )

        category = ProductCategory.objects.create(name=name)

        serializer = ProductCategorySerializer(category)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UniqueCategoryAPIView(GenericAPIView):
    permission_classes = [UserHavePermission]

    def delete(self, request, id):
        try:
            category = ProductCategory.objects.get(pk=id)
        except ProductCategory.DoesNotExist:
            return Response({
                'message': 'category not found'
            }, status=status.HTTP_400_BAD_REQUEST)

        category.delete()

        return Response(None)

    def put(self, request, id):
        affected_rows = ProductCategory.objects.filter(id=id).update(
            name=request.data.get('name')
        )

        if affected_rows > 0:
            return Response(None)
        return Response({
                'message': 'category not found'
            }, status=status.HTTP_400_BAD_REQUEST)


class ProductView(View):
    template = 'products/index.html'

    def get(self, request):
        cat_filter = request.GET.get('filter', 0)

        try:
            category = ProductCategory.objects.get(pk=cat_filter)

            products = Product.objects.filter(category=category.id)

            if products is None:
                raise Product.DoesNotExist
        except Product.DoesNotExist:
            products = Product.objects.select_related('category')
        except ProductCategory.DoesNotExist:
            products = Product.objects.select_related('category')

        categories = ProductCategory.objects.all()

        serializer = ProductSerializer(products, many=True)
        cat_serializer = ProductCategorySerializer(categories, many=True)

        data = []

        for product in serializer.data:
            product['images'] = get_product_images(product['id'], get_req_url(request))

            data.append(product)

        return render(
            request,
            self.template,
            {
                'products': data,
                'categories': cat_serializer.data,
                'selected_filter': cat_filter.__str__()
            }
        )


class UniqueProductView(View):
    template = 'products/show.html'
    error_404_template = 'products/404.ht'

    def get(self, request, id):
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return render(request, self.error_404_template)

        serializer = ProductSerializer(product)

        data = serializer.data

        category = ProductCategory.objects.get(pk=product.category.id)
        cat_serializer = ProductCategorySerializer(category)

        data['category'] = cat_serializer.data
        data['images'] = get_product_images(product.id, get_req_url(request))

        return render(
            request,
            self.template,
            {'product': data}
        )


class LoginView(View):
    template = 'manager/login.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class ManagerProductsView(View):
    template = 'manager/products/index.html'

    def get(self, request):
        data = get_product_list(request)

        return render(
            request,
            self.template,
            {'products': data}
        )


class ManagerAddProductView(View):
    template = 'manager/products/add.html'

    def get(self, request):
        categories = ProductCategory.objects.all()

        serializer = ProductCategorySerializer(categories, many=True)

        return render(
            request,
            self.template,
            {'categories': serializer.data}
        )


class ManagerEditProductView(View):
    template = 'manager/products/edit.html'
    error_404_template = 'manager/products/404.html'

    def get(self, request, id):
        try:
            product = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return render(
                request,
                self.error_404_template,
            )

        categories = ProductCategory.objects.all()

        cat_serializer = ProductCategorySerializer(categories, many=True)
        prod_serializer = ProductSerializer(product)

        data = prod_serializer.data

        data['images'] = get_product_images(id, get_req_url(request))

        return render(
            request,
            self.template,
            {
                'product': data,
                'categories': cat_serializer.data
            }
        )


class ManagerCategoriesView(View):
    template = 'manager/categories/index.html'

    def get(self, request):
        categories = ProductCategory.objects.all()

        serializer = ProductCategorySerializer(categories, many=True)

        ordered_list = sorted(serializer.data, key=lambda k: k['id'])

        return render(
            request,
            self.template,
            {'categories': ordered_list}
        )


def get_product_list(request):
    products = Product.objects.select_related('category')

    serializer = ProductSerializer(products, many=True)

    data = []

    for product in serializer.data:
        product['images'] = get_product_images(product['id'], get_req_url(request))

        data.append(product)

    return data


def get_product_images(product_id, url):
    product_images = ProductImage.objects.filter(product_id=product_id)
    images_serializer = ProductImageSerializer(product_images, many=True)

    for index in range(len(images_serializer.data)):
        images_serializer.data[index]['image'] = f'{url}{images_serializer.data[index]["image"]}'

    return images_serializer.data
