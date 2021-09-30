from django.urls import path
from . import views
from .views import CartUpdateView, tarikhL

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('tarikhl/', tarikhL, name="tarikhche"),
    # path('book/<int:pk>/', views.book, name="book"),
    path('<str:pk>/change/', CartUpdateView.as_view(), name="changestatus"),

]
