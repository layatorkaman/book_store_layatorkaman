from django.contrib.auth import views
from django.urls import path
from django.views.generic import TemplateView

from product.views import adminlte
from .views import SignupPageView, my_view, staff_page, form_info, BookCreate, CategoryCreate, DiscountAmountCreate, \
    PercentDiscountCreate, AddressCreateView, AddressListView, AddressUdateView, AddressDetail

# app_name="accounts"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', SignupPageView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('lte/', adminlte, name="adminlte"),
    path('staff/', staff_page.as_view(), name="staff"),
    path('redai/', my_view, name="redai"),
    path('form_info/', form_info.as_view(), name="form_info"),
    path('book/create/', BookCreate.as_view(), name="book_create"),
    path('address/', AddressCreateView.as_view(), name="address"),
    path('show/address/', AddressListView.as_view(), name='custom_add'),
    path('<str:pk>/edit/', AddressUdateView.as_view(), name='adredit'),

    path('discount/create/', DiscountAmountCreate.as_view(), name="discount_new"),
    path('discountp/create/', PercentDiscountCreate.as_view(), name="discount_percent_new"),
    path('category/create/', CategoryCreate.as_view(), name="category_create"),

]
