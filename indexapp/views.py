from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render,HttpResponse,redirect
from indexapp.models import TBook,TClass,TUser
import random,string
# from indexapp.captcha.image import ImageCaptcha
import uuid,os

# Create your views here.

def index(request):
    class1 = TClass.objects.filter(class_pid= None)
    class2 = TClass.objects.filter(class_pid__in=(a for a in range(1,100)))

    book1 = TBook.objects.order_by('shelves_date').exclude()[:8]
    book2 = TBook.objects.order_by('sales').exclude()[:5]
    book3 = TBook.objects.order_by('customer_score').exclude()[:10]

    book4 = TBook.objects.order_by( 'sales').exclude()[:10]
    status1 = request.GET.get('status')



    if status1 == '0':
        request.session['login'] = ''

    status = request.session.get('login')
    if status:
        uname = request.session.get('uname')
        return render(request, 'index.html',
                      {'class1': class1, 'class2': class2, 'book1': book1, 'book2': book2, 'book3': book3,
                       'book4': book4, 'uname': uname,'status':'1'})
    else:
        return render(request, 'index.html',
                      {'class1': class1, 'class2': class2, 'book1': book1, 'book2': book2, 'book3': book3,
                       'book4': book4,'status':'0'})





def details(request):
    book_id1 = request.GET.get('book_id')
    request.session['book_id'] = book_id1
    book_id2 = request.session.get('book_id')
    print(book_id1,book_id2)
    book = TBook.objects.get(book_id=int(book_id2))
    if book.series_name:
        series = '是'
    else:
        series = '否'

    bookpid = book.book_class.class_pid
    bookclan = book.book_class.class_name
    if bookpid:
        bookclpn = TClass.objects.get(class_id=bookpid).class_name
    else:
        bookclpn = bookclan

    bookzhe = int(book.dd_price/book.price*1000)/100
    status1 = request.GET.get('status')

    if status1 == '0':
        request.session['login'] = ''

    status = request.session.get('login')
    if status:
        uname = request.session.get('uname')
        return render(request, 'Book details.html',
                      {'book': book, 'series': series, 'bookclan': bookclan, 'bookclpn': bookclpn, 'bookzhe': bookzhe,'uname':uname,'status':'1'})


    return render(request,'Book details.html',{'book':book,'series':series,'bookclan':bookclan,'bookclpn':bookclpn,'bookzhe':bookzhe,'status':'0'})








def booklist(request):
    bclassp = request.GET.get('bclassp')
    bclass = request.GET.get('bclass')

    class1 = TClass.objects.filter(class_pid=None)
    class2 = TClass.objects.filter(class_pid__in=(a for a in range(1, 100)))



    number = request.GET.get('number')
    if not number:
        number = 1
    if bclassp or bclass:
        request.session['bclassp'] = bclassp
        request.session['bclass'] = bclass
    else:
        bclassp = request.session.get('bclassp')
        bclass = request.session.get('bclass')
    if bclass is None:
        tc = TClass.objects.filter(class_pid=bclassp)
        book = TBook.objects.filter(book_class__in=tc)

    else:
        tc = TClass.objects.filter(class_id=bclass)
        book = TBook.objects.filter(book_class=bclass)
    pagtor = Paginator(book, per_page=6)
    page = pagtor.page(number)

    bclassp1 = request.session.get('bclassp')
    bclasspn = TClass.objects.get(class_id=bclassp1).class_name

    if bclass:
        bclassn = TClass.objects.get(class_id=bclass).class_name
    else:
        bclassn = bclasspn

    status1 = request.GET.get('status')

    if status1 == '0':
        request.session['login'] = ''

    status = request.session.get('login')
    if status:
        uname = request.session.get('uname')
        return render(request, 'booklist.html',
                      {'class1': class1, 'class2': class2, 'bclass': bclass, 'bclassp': bclassp, 'page': page, 'tc': tc,
                       'bclasspn': bclasspn, 'bclassn': bclassn,'uname':uname,'status':'1'})




    return render(request,'booklist.html',{'class1':class1,'class2':class2,'bclass':bclass,'bclassp':bclassp,'page':page,'tc':tc,'bclasspn':bclasspn,'bclassn':bclassn,'status':'0'})











