"""bookstore_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.contrib import admin
from django.templatetags.static import static
from django.urls import path,include
from django.views import View

from accounts import views
from accounts.views import staff_page
from product.views import pageone

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home_customer/', views.home.as_view(), name='home'),
    path('', pageone , name='pageone'),
    path('store/', include('store.urls') , name="store"),
    path('product/', include('product.urls')),
    path('accounts/', include('accounts.urls') , name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('staff_page/',views.staff_page.as_view() , name="staff_page"),


]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)