from api.urls import path
from .views import BookCreateView, BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='list'),
    path('books/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
    path('books/create', BookCreateView.as_view(), name='create'),
]


