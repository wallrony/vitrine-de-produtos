from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vitrine_produtos.core.views import ProductView, UniqueProductView, \
    LoginView, ManagerProductsView, ManagerAddProductView,\
    ManagerEditProductView, ManagerCategoriesView


api_urls = [
    path('accounts/', include('vitrine_produtos.accounts.urls')),
    path('core/', include('vitrine_produtos.core.urls'))
]

urlpatterns = [
    # API Routes
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),

    # View Routes
    path('', ProductView.as_view()),
    path('product/<int:id>', UniqueProductView.as_view()),
    path('manager/login/', LoginView.as_view()),
    path('manager/products/', ManagerProductsView.as_view()),
    path('manager/products/add', ManagerAddProductView.as_view()),
    path('manager/products/edit/<int:id>', ManagerEditProductView.as_view()),
    path('manager/categories/', ManagerCategoriesView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
