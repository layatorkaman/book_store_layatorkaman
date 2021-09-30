from django.db import models
from django.urls import reverse
from extentions.utils import jalali_converter
from django.utils.html import format_html

# Create your models here.



class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='دسته بندي كتاب')
    slug = models.SlugField(max_length=30, unique=True, verbose_name="ادرس دسته بندي")

    class Meta:
        verbose_name = "دسته بندي كتاب "
        verbose_name_plural = 'دسته بندي كتاب ها'

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان كتاب')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس كتاب ')
    category = models.ManyToManyField(Category,verbose_name='دسته بندي')
    author = models.CharField(max_length=140, null=True, blank=True, verbose_name='نويسنده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ايجاد')
    inventory = models.IntegerField(verbose_name='موجودي ')
    price=models.BigIntegerField(verbose_name='قيمت')
    img=models.ImageField(upload_to='image',verbose_name= 'عكس',  null=True , blank=True )
    discountAmount=models.ForeignKey('store.DiscountAmount' , on_delete=models.CASCADE , null=True , blank=True)
    percentDiscount=models.ForeignKey('store.PercentDiscount' , on_delete=models.CASCADE ,null=True , blank=True )


    class Meta:
        verbose_name = 'كتاب'
        verbose_name_plural = 'كتاب ها'

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description="تاريخ ايجاد"

    def img_tag(self):
        return format_html("<img  width=70px height=70px style='border-radius:5px;' src='{}'>".format(self.img.url) )
    img_tag.short_description="عكس "



    def new_price(self):

        if self.discountAmount:
            price = self.price - self.discountAmount.amount_dis
            return price
        elif self.percentDiscount:
            price = self.price - self.price*self.percentDiscount.percent
            return price
        else:
            return self.price

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('bookdetail', args=[str(self.slug)])