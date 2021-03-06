from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('cart/confirmation', views.confirmation, name='confirmation'),
    path('items', views.items, name='items'),
    path('item/<int:id>', views.item, name='item'),
    path('item/<int:id>/add', views.add_item, name='add_item'),
    path('item/<int:id>/remove', views.remove_item, name='remove_item'),
    path('item/<int:id>/remove-all', views.remove_all, name='remove_all'),
    path('orders', views.order_list, name='order_list'),
    path('orders/<int:id>', views.view_order, name='view_order')
]
