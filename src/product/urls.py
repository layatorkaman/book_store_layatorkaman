

from product.views import BookList, BookDetail, SearchList, cat_book, BookUpdate, BookFormView, BookList2, \
    BookDeleteView

BookDeleteView
from django.urls import path


from . import views

urlpatterns = [
    path('book_list/', BookList2.as_view(), name='book_list2'),
    path('book_edit/<int:pk>', BookUpdate.as_view(), name='book_edit'),
    path('<str:slug>/edit/', BookFormView.as_view(), name='BookFormView'),
    path('<str:slug>/del/', BookDeleteView.as_view(), name='BookDeleteView'),
    path('<str:slug>/', BookDetail.as_view(), name='bookdetail'),
    path('dastan/dd/', views.cat_book , name='dastan'),
    path('sheer/dd', views.cat_sheer , name='sheer'),
    path('elmi/dd', views.cat_elmi , name='elmi'),
    path('khareji/dd', views.cat_khareji , name='khareji'),
    path('search/', SearchList.as_view(), name='search'),
    path('search/page/', SearchList.as_view(), name='search'),





    ]