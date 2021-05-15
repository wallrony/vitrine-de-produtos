from django.urls import path

from vitrine_produtos.accounts import views

urlpatterns = [
    path('login/', views.AuthenticationAPIView.as_view()),
    path('register/', views.UserApiView.as_view())
]
