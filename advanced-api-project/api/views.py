from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book 
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,  IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    This view is opem to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterest_fields = ['publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a specific book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Add a new book. Resticted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Modifies an existing book. Restricted to aunthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]