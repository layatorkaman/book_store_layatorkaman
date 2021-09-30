from datetime import timezone

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from rest_framework.permissions import IsAdminUser
from urllib3 import request

from product.models import Book, Category
from store.models import DiscountAmount, PercentDiscount
from .models import Customer, Address

from .form import CustomUserCreationForm, AddressForm


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# @login_required(login_url='login')
class home(TemplateView):
    template_name = 'registration/home_customer.html'


class staff_page(TemplateView):
    template_name = 'staff_page.html'


class form_info(TemplateView):
    template_name = 'form_info.html'


def my_view(request):
    if request.user.is_staff == True and request.user.is_superuser == False:
        return redirect("staff")
    if request.user.is_superuser:
        return redirect("adminlte")

    if request.user.is_superuser == False and request.user.is_staff == False:
        return redirect("home")


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book

    fields = "__all__"
    template_name = "book_create_update.html"


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name_suffix = '_update_form'


class CategoryCreate(CreateView):
    model = Category

    fields = "__all__"
    template_name = "category_create.html"
    success_url = '/accounts/staff/'


class DiscountAmountCreate(LoginRequiredMixin, CreateView):
    model = DiscountAmount

    fields = "__all__"
    template_name = "new_discount_amoun.html"
    success_url = '/accounts/staff/'


class PercentDiscountCreate(LoginRequiredMixin, CreateView):
    model = PercentDiscount

    fields = "__all__"
    template_name = "new_discount_percent.html"
    success_url = '/accounts/staff/'


class AddressCreateView(CreateView):
    model = Address
    fields = "__all__"

    template_name = 'address_form.html'
    success_url = '/home_customer/'


class AddressListView(ListView):
    model = Address
    template_name = 'custom_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class AddressFormView(UpdateView):
#     model = Address
#     template_name = 'custom_add.html'
#     form_class = AddressForm
#
#     def get_success_url(self):
#         return reverse_lazy('address_detail', args=[str(self.object.pk)])
#

class AddressUdateView(UpdateView):
    model = Address
    fields = "__all__"
    template_name = 'address_detail.html'
    success_url = '/home_customer/'


class AddressDetail(DetailView):
    model = Address
    template_name = 'address_detail.html'
