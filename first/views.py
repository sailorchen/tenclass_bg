import datetime

import jwt
from django.shortcuts import render
from rest_framework.views import APIView
from .models import shop_user
from django.http import JsonResponse
import json
import uuid
from first.base import Base
from first.models import env_table,src_table
from django_filters.rest_framework import DjangoFilterBackend
from operator import methodcaller

# Create your views here.
def get_jwt_token(user_name, role_data='default', JWT_SECRET_KEY=None):
    """
    生成jwt-token
    :param unit_name:
    :param role_data:
    :return:
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=3600),  # 单位秒
        'iat': datetime.datetime.utcnow(),
        'data': {'username': user_name, 'role_data': role_data}
    }
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return str(encoded_jwt, encoding='utf8')

# 登录api
class LoginView(APIView):
    def post(self, request, format=None):
        """
        通过APIView实现登录
        """
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if shop_user.objects.filter(username=username,password=password):
            return JsonResponse({"code":200,'msg':"登录成功","token":uuid.uuid4()})
        return JsonResponse({"code":400,"msg":"用户不存在"})


# 菜单列表api
class MenuView(APIView):
    def get(self, request, format=None):
        """
        通过APIView实现登录
        """
        data = {"code":200,"msg":"获取菜单成功",'data':[
            {'id':"114",'menuName':'用户管理','children':[{'id':55,'subName':'用户列表','path':'users'}]},
            {'id':"115",'menuName':'课程管理','children':[{'id':35,'subName':'引流课','path':'roles'},{'id':56,'subName':'交付课','path':'permissions'}]}
        ]}
        return JsonResponse(data)

#   用户信息api
class UserList(APIView):
    def get(self, request, format=None):
        """
        通过APIView实现登录
        """
        data = {"code":200,"msg":"获取列表成功",'data':[
            {'id':"114",'username':'刘德华','mobile':'135353553','email':'253252@q','address':'哈哈哈','status':True},
            {'id':"115",'username':'刘德华1','mobile':'135353553','email':'253252@q','address':'哈哈哈','status':True},
            {'id': "116", 'username': '刘德华2', 'mobile': '135353553', 'email': '253252@q', 'address': '哈哈哈',
             'status': True},
            {'id': "117", 'username': '刘德华3', 'mobile': '135353553', 'email': '253252@q', 'address': '哈哈哈',
             'status': True},
        ]}
        return JsonResponse(data)

class Run_Script(APIView):

    # filter_backends = [DjangoFilterBackend]
    # filter_fileds = ['page_name','src_name']

    def get(self,request,format=None):
        page_name = request.GET.get("page_name")
        src_name = request.GET.get("src_name")
        b=Base()
        methodcaller(src_name)(b)
        return JsonResponse({'data':200})

    def post(self,request,format=None,**kwargs):
        body = json.loads(request.body)
        b=Base()
        src_name = body.get("src_name")
        # token = body.get("token")
        # env = body.get("env")
        # shop = body.get("shop_id")
        methodcaller(src_name, **body)(b)
        # methodcaller(src_name,token=token,env=env,shop=shop)(b)
        return JsonResponse({'code': 200,'msg':'运行成功','data':[]})


class list_shop(APIView):
    filter_backends = [DjangoFilterBackend]
    filter_fileds = ['env']
    def get(self,request):
        try:
            env = request.GET.get("env")
            envs=env_table.objects.filter(env=env).values('shop','shop_label').order_by('id')
            res = list(envs)
            return JsonResponse({"code": 200, "msg": "成功","data":res})
        except Exception as e:
            return JsonResponse({"code":400,"msg":"错误"})

class src_info(APIView):

    filter_backends = [DjangoFilterBackend]
    filter_fileds = ['page_name']
    def get(self,request):
        page_name = request.GET.get("page_name")
        te = src_table.objects.filter(src_page=page_name,is_delete=0).values('id','src_name','src_desc','src_label')
        res = list(te)
        return JsonResponse({"code": 200, "msg": "成功","data":res})

