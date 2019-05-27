from django.urls import path,include
from userapp import views
from indexapp import views as views1

# app_name = 'userapp'
urlpatterns =[
    path('login/',views.login,name='login'),
    path('login1/',views.login1,name = 'login1'),
    path('register1/', views.register1,name='register1'),
    path('register/',views.register,name='register'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('checkname/',views.checkname,name='checkname'),
    path('checkcaptcha/',views.checkcaptcha,name='checkcaptcha'),
    path('details/', views1.details, name='details'),
    path('index/',views1.index,name='index'),
    path('register_ok',views.register_ok,name = 'register_ok'),
]