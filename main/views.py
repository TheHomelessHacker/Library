from django.db.models import Count
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    # Аннотируем количество заказов для каждой книги
    books = Book.objects.annotate(orders_count=Count('order'))

    if books.exists():
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response('The book list is empy! Create a book!')


class CreateBookView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Книга успешно создана')

class BookDetailsView(generics.RetrieveAPIView):
    queryset = Book.objects.annotate(orders_count=Count('order'))
    serializer_class = BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.annotate(orders_count=Count('order'))
    serializer_class = BookSerializer


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    # Prefetch_related для оптимизации загрузки связанных книг
    queryset = Order.objects.prefetch_related('books')
    serializer_class = OrderSerializer
