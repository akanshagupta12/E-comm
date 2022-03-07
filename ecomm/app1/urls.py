from encodings import search_function
from django.urls import path 
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('products/', product_view , name='products'),
    # path('cart',cart_view,name='cart'),
    path('additem/<int:pk>/',add_item_to_cart,name='cart'),
    path('additemincart/<int:pk>/',add_quantity_in_cart,name='remove_item'),
    path('subitem/<int:pk>/',remove_quantity_in_cart,name='remove_item'),
    path('deleteitemincart/<int:pk>/',delete_item_from_cart,name='delete_item'),
    # path('additem/<int:   pk>/',add_item_to_cart,name='cart'),
    path('order/',cart_page,name='order'),
    path('count_item/',count_item,name='count'),
    path('payment/',payment,name='payment'),
    # path('redirect',payment_redirect,name='redirect'),
    path('payment/success/', success , name= "payment handler") , 
    path('customer/form/', customer_form , name= "payment handler"),
    path('item/<int:pk>/', item_details , name= "item") , 
    path('send_mail/', sending_mail , name= "send_mail") ,
    path('search/', search , name= "send_mail") ,
    path('item_cart/<int:pk>/', add_in_cart , name= "add_item_in_cart") ,
]