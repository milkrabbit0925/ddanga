from django.shortcuts import render, redirect,HttpResponse
from django.utils.deprecation import MiddlewareMixin
from userapp.views import login
import re


class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("init1")

    # view处理请求前执行
    def process_request(self, request):
        if 'indent/' in request.path  :
            status=request.session.get('login')
            # status=''
            if status:
                print('正在登录')
            else:
                return redirect('login')


    # 在process_request之后View之前执行
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("view:", request, view_func, view_args, view_kwargs)

    # view执行之后，响应之前执行
    def process_response(self, request, response):
        path = request.path
        print('---------中间件-----------', path)

        path = request.path  # 每次请求的路径
        if re.findall('^/indexapp/', path) or re.findall('^/carapp/', path) or re.findall('^/userapp/', path):  # 当为其他模块的请求时，记录路径
            print('备选的path----------', request.path)
            request.session['path'] = request.path
        return response  # 必须返回response

    # 如果View中抛出了异常
    def process_exception(self, request, ex):  # View中出现异常时执行
        print("exception:", request, ex)