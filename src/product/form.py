from django import forms

from product.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields=['title','author','inventory','price']



