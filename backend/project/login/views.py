from django.shortcuts import render
from django.http import JsonResponse
from common.models import User
import json
# Create your views here.

def create(request):
     if request.method == 'POST':
          ret = {'code':100, 'msg':None}
          username = request.POST.get('username')
          password = request.POST.get('password')
          usertype = request.POST.get('usertype')
          obj = User.objects.filter(uesrname = username).first()
          if not obj:
               User.objects.create(username=username ,password=password,usertype = usertype)
               ret['code'] = 100
               ret['msg'] = '创建成功'
          else:
               ret['code'] = 101
               ret['msg'] = '用户已存在'

     return JsonResponse(ret)

def login(request):
     if request.method == 'POST':
          ret = {'code':1000,'msg':None}
          request.params = json.loads(request.body)
          username = request.params['username']
          password = request.params['password']
          obj = User.objects.filter(username = username,password=password).first()
          if not obj:
               ret['code'] = 1001
               ret['msg'] = '用户名或密码错误'
          else:
               ret['code'] = 1000
               ret['msg'] = '登录成功'
     
     return JsonResponse(ret)

def show(request):
     qs = User.objects.values()
     relist=list(qs)
     return JsonResponse({'relist':relist})