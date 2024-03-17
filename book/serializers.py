from rest_framework import serializers
from .models import Book


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Book

        fields = (
            'id',
            'title',
            'writer',
            'rating',
            'number_of_editions',
        )
