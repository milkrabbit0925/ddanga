import datetime
import hashlib

from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

from ddang import settings
from indexapp.models import TBook, TClass, TUser, Check_user
from django.shortcuts import render,HttpResponse,redirect
from userapp.captcha.image import ImageCaptcha
import uuid,os,re
import random,string
from django.db import transaction

# Create your views here.



def login(request):
    uname = request.session.get('uname')
    upwd = request.session.get('upwd')
    result = TUser.objects.filter(email=uname, password=upwd)
    if result:
        request.session['login'] = 'ok'
        path = request.session.get('path')

        return redirect(path)

        # return redirect('index')
    return render(request,'login.html')



def login1(request):
    uname = request.POST.get('txtUsername')
    upwd = request.POST.get('txtPassword')
    # captcha = request.POST.get('captcha')
    # code = request.session.get('code')

    result=TUser.objects.filter(username=uname, password=upwd)

    if result :
        uid = TUser.objects.get(email=uname).user_id
        print(uid)
        request.session['uid'] = uid
        request.session['login'] = 'ok'
        path = request.session.get('path')



        return redirect(path)
    return HttpResponse('登陆失败')




def register(request):
    status = request.session.get('login')

    if status:
        return redirect('index')
    else:

        return render(request, 'register.html')








def checkname(request):
    username = request.GET.get('username')
    result = TUser.objects.filter(email=username)
    if result:


        return HttpResponse('1')


    else:
        request.session['checkname'] = 'ok'
        return HttpResponse('0')



def getcaptcha(request):
    image=ImageCaptcha()
    rand_code=random.sample(string.ascii_letters+string.digits,4)
    rand_code=''.join(rand_code)
    data=image.generate(rand_code)
    request.session['code']=rand_code
    return HttpResponse(data,'image/png')



def checkcaptcha(request):
    captcha = request.GET.get('captcha')
    code = request.session.get('code')
    print('验证码',code,captcha)
    if captcha.upper() == code.upper():
        request.session['checkcap'] = 'ok'
        return HttpResponse('0')
    else:
        return HttpResponse('1')


def has_code(name,now):
    h = hashlib.md5()
    name += now
    h.update(name.encode())
    return h.hexdigest()

def make_check_user(new_user):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    code = has_code(new_user.email,now)
    Check_user.objects.create(code=code,user=new_user)
    return code


def send_email(email,code):
    subject='来自DD的邮件'
    from_email = 'zdx_email@sina.com'
    text_content = '欢迎访问http://127.0.0.1:8000/userapp/email_check/，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target=blank>http://127.0.0.1:8000/userapp/email_check/</a>，\欢迎你来验证你的邮箱，验证结束你就可以登录了！</p>'.format('127.0.0.1',code)
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def register1(request):
    # try:
    #     with transaction.atomic():
    uname = request.POST.get('txt_username')
    upwd = request.POST.get('txt_password')
    checkcap = request.session.get('checkcap')
    checkname = request.session.get('checkname')
    if checkcap and checkname :
        result=TUser.objects.create(email=uname,username=uname,password=upwd)
        if result:
            request.session['uname'] = uname
            request.session['upwd'] = upwd
            request.session['login'] = 'ok'
            # return redirect('login')
            code = make_check_user(result)
            send_email(uname, code)
            return redirect('register_ok')
    return HttpResponse('注册失败1')
    # except:
    #     return HttpResponse('注册失败2')


def register_ok(request):


    status = request.session.get('login')
    if status:
        uname = request.session.get('uname')
        return render(request, 'register ok.html',{ 'uname': uname, 'status': '1'})
    else:
        return redirect('login')











