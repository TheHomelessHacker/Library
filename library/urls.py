from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from main.views import (books_list, CreateBookView, BookDetailsView, BookUpdateView,
                        BookDeleteView, OrderViewSet)

router = SimpleRouter()
router.register('orders', OrderViewSet, 'orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', books_list),
    path('api/v1/books/create/', CreateBookView.as_view()),
    path('api/v1/books/<int:pk>/', BookDetailsView.as_view()),
    path('api/v1/books/update/<int:pk>/', BookUpdateView.as_view()),
    path('api/v1/books/delete/<int:pk>/', BookDeleteView.as_view()),
    path("api/v1/", include(router.urls))
]
