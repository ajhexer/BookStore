from django.urls import path
from books.views import BookListView, BookDetailView, SearchView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchView.as_view(), name='search_results')
]