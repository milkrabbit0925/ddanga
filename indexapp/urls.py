from django.urls import path
from indexapp import views
from userapp import views as view1

# app_name = 'indexapp'
urlpatterns =[
    path('index/',views.index,name='index'),
    path('details/',views.details,name='details'),
    path('booklist/',views.booklist,name='booklist')
]