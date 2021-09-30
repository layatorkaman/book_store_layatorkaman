from django.contrib.auth import get_user_model
from django.db import models
from extentions.utils import jalali_converter

# Create your models here.
from accounts.models import Customer, Address
from product.models import Book


class DiscountAmount(models.Model):
    amount_dis = models.BigIntegerField(verbose_name='مقدار تخفيف')
    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, default=None,
                                verbose_name='ايجاد كننده تخفيف')
    time = models.DateTimeField(verbose_name='شروع تخفيف')
    expire_date = models.DateTimeField(verbose_name='انقضاء تخفيف')

    class Meta:
        verbose_name = "تخفيف نقدي "
        verbose_name_plural = "تخفيفات نقدي "

    def jtime(self):
        return jalali_converter(self.time)

    def jexpire_date(self):
        return jalali_converter(self.expire_date)

    def __str__(self):
        return f"{self.creator}"


class PercentDiscount(models.Model):
    percent = models.IntegerField(verbose_name='درصد تخفيف ')
    date_from = models.DateTimeField(verbose_name='تاريخ ايحاد')
    date_valid = models.DateTimeField(verbose_name='تاريخ اعتبار')
    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, default=None,
                                verbose_name='ايجاد كننده ')
    active = models.BooleanField()

    class Meta:
        verbose_name = "تخفيف درصدي  "
        verbose_name_plural = "تخفيفات درصدي  "

    def jdate_from(self):
        return jalali_converter(self.date_from)

    def jdate_valid(self):
        return jalali_converter(self.date_valid)

    def __str__(self):
        return f"{self.creator}"


class CopounDiscount(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='كد')
    valid_from = models.DateTimeField(verbose_name='زمان شروع')
    valid_to = models.DateTimeField(verbose_name='زمان انقضاء')
    discount = models.IntegerField(verbose_name='مقدار تخفيف')
    active = models.BooleanField()

    class Meta:
        verbose_name = 'كوپن تخفيف'
        verbose_name_plural = 'كوپن هاي تخفيف'
    def jvalid_from(self):
        return jalali_converter(self.valid_from)

    def jvalid_to(self):
        return jalali_converter(self.valid_to)


    def __str__(self):
        return f"{self.code}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='سبد خريد')

    class Meta:
        verbose_name = 'سبد خريد'
        verbose_name_plural = 'سبدهاي خريد'

    def __str__(self):
        return f"{self.customer}"


class Order(models.Model):
    STATUS = (('R', 'ثبت'), ('T', 'سفارش'))
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, verbose_name='مشتري')
    date_ordered = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ ايجاد')
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True , blank=True)
    status = models.CharField(choices=STATUS, default='T', max_length=1, verbose_name='وضعيف سفارش')
    delivery_address = models.ForeignKey('accounts.Address',
                                         verbose_name='آدرس سفارش',
                                         on_delete=models.DO_NOTHING,
                                         related_name='order_addresses', blank=True, null=True)
    cart = models.ForeignKey(Cart, verbose_name='سبد خرید',
                             on_delete=models.CASCADE,
                             related_name='cartorders' , null=True)

    class Meta:
        verbose_name="مورد"
        verbose_name_plural="موارد"



    def jdate_ordered(self):
        return jalali_converter(self.date_ordered)

    jdate_ordered.short_description = "زمان سفارش"

    def __str__(self):
        return f"{self.id}"

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING,  verbose_name=' كتاب')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name='موجودي')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ ايجاد')


    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def jdate_added(self):
        return jalali_converter(self.date_added)



    @property
    def get_total(self):
        total = self.book.new_price() * self.quantity
        return total
