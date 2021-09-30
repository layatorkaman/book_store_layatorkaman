from django.contrib import admin

# Register your models here.
from store.models import DiscountAmount, PercentDiscount, CopounDiscount, Order, OrderItem, Cart


class DiscountAmountAdmin(admin.ModelAdmin):
    list_display = ['amount_dis', 'creator', 'jtime', 'jexpire_date', ]
    list_filter = ['amount_dis', 'creator']
    search_fields = ['amount_dis', 'creator']


admin.site.register(DiscountAmount, DiscountAmountAdmin)


class PercentDiscountAdmin(admin.ModelAdmin):
    list_display = ['percent', 'jdate_from', 'jdate_valid', 'creator', 'active']
    list_filter = ['percent', 'creator']
    search_fields = ['percent', 'creator']


admin.site.register(PercentDiscount, PercentDiscountAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'jdate_ordered', 'status','delivery_address']
    list_filter = ['customer', ]
    search_fields = ['customer',]


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['book', 'order', 'quantity', 'jdate_added']
    list_filter = ['book', ]


admin.site.register(OrderItem, OrderItemAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ["customer", ]
    list_filter = ["customer", ]


admin.site.register(Cart, CartAdmin)


class CopounDiscountAdmin(admin.ModelAdmin):
    search_fields = ['code']


admin.site.register(CopounDiscount, CopounDiscountAdmin)
