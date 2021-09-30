from django.conf import settings

from accounts.models import Address


def address_cus(request):
    sq=Address.objects.filter(customer=request.user)
    return {
        'add_cus':sq


    }