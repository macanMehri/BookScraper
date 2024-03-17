from django.urls import path, include
from .views import BookViewSet, scrape_view
from rest_framework import routers


book_router = routers.DefaultRouter()
book_router.register('', BookViewSet)

urlpatterns = [
    path('api/', include(book_router.urls,)),
    path('scrape/', scrape_view),
]
