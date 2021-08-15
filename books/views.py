from django.shortcuts import render
from django.views.generic import ListView, DetailView
from books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'


class SearchView(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
            return None
