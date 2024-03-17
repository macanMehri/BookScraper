from django.shortcuts import render, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, permissions
from .serializers import BookSerializer
from .models import Book
from .scraper import scrape


def scrape_view(request):
    scrape(number_of_pages=1)
    return HttpResponse('Data scraped seccussfully')


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.filter(is_active=True,).order_by('pk')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = (
        'id',
        'number_of_editions',
        'created_date',
    )
    search_fields = (
        'id',
        'title',
        'writer',
    )
