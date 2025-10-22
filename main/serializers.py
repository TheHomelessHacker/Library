from rest_framework import serializers
from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    orders_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, 'orders_count'):
            representation['orders_count'] = instance.orders_count
        else:
            representation['orders_count'] = instance.orders.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        books = instance.books.all()
        representation['books'] = [
            {
                "author": book.author,
                "title": book.title,
                "year": book.year
            }
            for book in books
        ]
        return representation
