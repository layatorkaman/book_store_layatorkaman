from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json
import datetime

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import ListView, UpdateView

from accounts.models import Address, Customer
from product.models import Book
from .models import OrderItem, Order, CopounDiscount , Cart
from .utils import cartData, guestOrder
from .form import CopounDiscountForm


def store(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    books = Book.objects.all()
    context = {'books': books, 'cartItems': cartItems ,'order':order}
    return render(request, 'store.html', context)


def book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book = Book.objects.get(id=pk)
        try:
            customer = request.user
        except:
            device = request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, book=book)
        orderItem.quantity = request.POST['quantity']
        orderItem.save()
        return redirect('cart')
    context = {'book': book, 'price': book.new_price()}
    return render(request, 'book.html', context)


def cart(request):
    try:
        customer = request.user
        data = cartData(request)

        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'cart.html', context)

    except:

        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False , status="T")
    context = {'order': order}
    return render(request, 'cart.html', context)



def updateItem(request):
    if request.method == "POST":
        print(request.body)
        print(request.is_ajax())
        from pprint import pprint
        pprint(dict(request.POST.items()))
        print('data : ', dict(request.POST.items()))
        data = json.loads(request.body)
        print(data)
        print(type(data))
        print(data['bookId'])
        bookId = data['bookId']
        action = data['action']



        customer = request.user
        book = Book.objects.get(id=bookId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False , status="T")


        orderItem, created = OrderItem.objects.get_or_create(order=order, book=book)

        print("order",orderItem.order)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)


        if action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()


        return JsonResponse('Item was added', safe=False)
    else:
        return HttpResponse("get method")


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()

    data = json.loads(request.body)

    if request.user.is_authenticated:

        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False , status="T")
    else:

        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()


class tarikhche(ListView):
    model = Order
    template_name = 'tarikhche.html'

    def get_query_set(self):
        return Order.objects.filter(cart__customer=self.request.user)


class CartUpdateView(UpdateView):
    model = Order
    template_name = "change_form.html"
    fields = ["delivery_address","delivery_address" ]
    success_url = '/store/'

    def form_valid(self, form):
        form.instance.status = "R"
        form.save()
        return super(CartUpdateView, self).form_valid(form)

def tarikhL(request):
    data= Order.objects.filter(customer= request.user)
    return render(request,'tarikhche.html',{'data':data})
