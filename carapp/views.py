from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from indexapp.models import *
from carapp.cart import Cart,Cartltem





def cart_add(request):
    book_id = request.GET.get('book_id')
    book = TBook.objects.get(book_id=book_id)
    amount = (int(request.GET.get('amount')) if request.GET.get('amount') else 1)
    cart = request.session.get('cart')
    info = Cartltem(book,amount)
    if cart == None:
        cart = Cart()
    cart.add_book_toCart(info)
    request.session['cart'] = cart
    return HttpResponse('ok')


def cart_remove(request):
    book_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    # print(book_id,2)
    cart.remove(book_id)
    request.session['cart'] = cart
    return HttpResponse('ok')


def cart_recover(request):
    book_id = request.GET.get('info_id')
    cart = request.session.get('cart')
    cart.recover(book_id)
    request.session['cart'] = cart
    return HttpResponse('ok')


def cart_change_amount(request):
    book_id = request.GET.get('info_id')

    new_amount = int(request.GET.get('new_amount'))
    cart = request.session.get('cart')
    # print(new_amount)
    cart.change_amount(book_id,new_amount)
    request.session['cart'] = cart
    return HttpResponse('ok')


def car(request):
    cart = request.session.get('cart')
    uname = request.session.get('uname')
    status = request.session.get('login')
    # print(cart.dd_price)
    # dd_price=cart.dd_price
    # print(dd_price)
    # print(cart.amount)
    if status:
        return render(request, 'car.html', {'cart': cart, 'uname': uname, 'status':'1'})
    else:
        return render(request, 'car.html', {'cart': cart, 'uname': uname, 'status':'0'})





def indent(request):
    cart = request.session.get('cart')
    uname = request.session.get('uname')
    uid = request.session.get('uid')
    add = TAdds.objects.filter(user_id=uid)
    print(uid)
    print(add)



    return render(request,'indent.html',{'cart':cart,'uname':uname,'add':add})


def checkadd(request):
    adid = request.POST.get('adid')
    add = TAdds.objects.filter(id=int(adid))[0]
    jstr = {'name': add.a_name, 'address': add.a_address, 'post': add.post_id, 'phone': add.mobile_phone}
    return JsonResponse(jstr)


def checkname(request):
    username = request.POST.get('input_user')
    if not username:
        return HttpResponse('empty')
    else:
        request.session['username'] = username
        return HttpResponse('ok')


def checkaddress(request):
    useraddress = request.POST.get('input_adress')
    if not useraddress:
        return HttpResponse('empty')
    else:
        request.session['useraddress'] = useraddress
        return HttpResponse('ok')


def checkcode(request):
    usercode = request.POST.get('input_code')
    if not usercode:
        return HttpResponse('empty')
    else:
        request.session['userpost'] = usercode
        return HttpResponse('ok')


def checkphone(request):
    userphone = request.POST.get('input_phone')
    if not userphone:
        return HttpResponse('empty')
    else:
        request.session['userphone'] = userphone
        return HttpResponse('ok')


def indentok(request):
    uid = request.session.get('uid')
    username = request.session.get('username')
    useraddress = request.session.get('useraddress')
    userpost = request.session.get('userpost')
    userphone =  request.session.get('userphone')
    result = TAdds.objects.create(a_name=username,a_address=useraddress,post_id=userpost,mobile_phone=userphone,user_id=uid)
    uname = request.session.get('uname')
    cart = request.session.get('cart')



    return render(request,'indent ok.html',{'uname':uname,'cart':cart,'username':username})




