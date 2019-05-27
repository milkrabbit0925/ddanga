from django.urls import path
from carapp import views
from userapp import views as view1
from indexapp import views as view2



urlpatterns =[
    path('car/',views.car,name='car'),
    path('cart_add/',views.cart_add,name='cart_add'),
    path('cart_remove/',views.cart_remove,name='cart_remove'),
    path('cart_change_amount/',views.cart_change_amount,name='cart_change_amount'),
    path('cart_recover/',views.cart_recover,name='cart_recover'),
    path('indent/', views.indent, name='indent'),
    path('checkadd/',views.checkadd,name='checkadd'),
    path('checkaddress/',views.checkaddress,name='checkaddress'),
    path('checkaname/',views.checkname,name='checkname'),
    path('checkcode/',views.checkcode,name='checkcode'),
    path('checkphone/',views.checkphone,name='checkphone'),
    path('indentok/',views.indentok,name='indentok'),

]

