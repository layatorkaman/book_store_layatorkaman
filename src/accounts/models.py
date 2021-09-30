from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.urls import reverse


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=80, null=True, blank=True, verbose_name='نام')
    last_name = models.CharField(max_length=80, null=True, blank=True, verbose_name='نام خانوادگي ')
    username = models.CharField(max_length=60,  unique=True,verbose_name= 'نام كاربري')
    password = models.CharField(max_length=20, verbose_name='پسورد')
    password_rep = models.CharField(max_length=20, verbose_name='تكرار پسورد')
    device = models.CharField(max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'كاربر'
        verbose_name_plural = 'كاربران'

    def __str__(self):
        return f"{self.username}"

class Owner_site(CustomUser):
    is_staff = True
    is_superuser = True

    class Meta:
        proxy = True
        verbose_name=" مالك سايت"
        verbose_name_plural="مالكان سايت "


class Staff(CustomUser):

    is_staff = True
    is_superuser = False

    class Meta:
        proxy = True
        verbose_name = " كارمند"
        verbose_name_plural = "كارمندان "



class Customer(CustomUser):
    is_superuser = False
    is_staff = False

    class Meta:
        proxy = True
        verbose_name = " كاربر سايت"
        verbose_name_plural = "كاربران  سايت "

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    city = models.CharField(max_length=200 , verbose_name='شهر ')
    street = models.CharField(max_length=200 , verbose_name= ' خيابان')
    postal_code = models.CharField(max_length=16 , verbose_name='كدپستي')
    address_line1=models.CharField(max_length=100 , verbose_name='ادرس اول')
    address_line2=models.CharField(max_length=100 , blank=True , null=True , verbose_name='ادرس دوم')
    status = models.BooleanField(default=False , verbose_name='وضعيت ')

    class Meta:
        verbose_name= 'آدرس'
        verbose_name_plural='آدرس ها '

    def __str__(self):
        return f"{self.city}"

    def get_absolute_url(self):
        return reverse('address_detail', args=[str(self.pk)])






