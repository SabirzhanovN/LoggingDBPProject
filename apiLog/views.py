from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .serializers import LoggingMovesSerializer
from shopApp.models import LoggingMoves


class LoggingMovesPageSize(PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    max_page_size = 1000


class LoggingMovesListAPIView(generics.ListAPIView):
    pagination_class = LoggingMovesPageSize
    queryset = LoggingMoves.objects.all()
    serializer_class = LoggingMovesSerializer

