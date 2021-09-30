from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from accounts.models import Address
from store.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2' , ]



class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        exclude=['customer',]



