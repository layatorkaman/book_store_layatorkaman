from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, FormView

from .form import BookForm
from .models import Book, Category


class BookList(ListView):
    model = Book
    template_name = 'store.html'
    context_object_name = 'books'
    # paginate_by = 2


class BookList2(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetail(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_edit.html'
    success_url = reverse_lazy('staff')


class SearchList(ListView):
    paginate_by = 2
    template_name = 'search_list.html'

    def get_queryset(self):
        search = self.request.GET.get('q')
        if Book.objects.filter(title__icontains=search):
            return Book.objects.filter(title__icontains=search)
        elif Book.objects.filter(author__icontains=search):
            return Book.objects.filter(author__icontains=search)
        else:
            return f"{'not fount'}"


def cat_book(request):
    books = Category.objects.get(title="داستان").book_set.all()

    context = {'books': books}
    return render(request, 'dastan.html', context)


def cat_sheer(request):
    books1 = Book.objects.filter(category__title="داستان")

    books = Category.objects.get(title="شعر").book_set.all()
    print(books)
    context = {'books': books}
    return render(request, 'sheer.html', context)


def cat_elmi(request):
    books = Category.objects.get(title="علمي").book_set.all()
    print(books)
    context = {'books': books}
    return render(request, 'elmi.html', context)


def cat_khareji(request):
    # books = Category.objects.get(title="خارجي").book_set.all()
    books = Book.objects.filter(category__title="ترجمه")
    print(books)
    context = {'books': books}
    return render(request, 'khareji.html', context)


def pageone(request):
    return render(request, 'page1.html')


def adminlte(request):
    return render(request, 'lte.html')


def staffpage(request):
    return render(request, 'staff_page.html')


class BookFormView(UpdateView):
    model = Book
    template_name = 'bookone.html'
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy('bookdetail', args=[str(self.object.slug)])


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('store')



