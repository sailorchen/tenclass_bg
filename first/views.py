import datetime

import jwt
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from django.http import JsonResponse
import json
from first.base import Base
from first.models import env_table,src_table,menu,submenu,shop_user
from django_filters.rest_framework import DjangoFilterBackend
from operator import methodcaller
import time
# Create your views here.
from first.seris import PagerSerialiser

#引入token
from first.authtoken import AuthenticationSelf
from first.models import Usertoken

# 登录api
class LoginView(APIView):
    authentication_classes = []
    #解析jwt-token
    # def test(self,token):
    #     try:
    #         data = jwt.decode(token,'chenhu0905',algorithms=['HS256'])
    #     except Exception as e:
    #         print(e)
    #     print(data)

    def post(self, request, format=None):
        """
        通过APIView实现登录
        """
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        user_id = shop_user.objects.filter(username=username, password=password, status=1).values('id')
        if user_id:
            id = user_id[0]
            token_dict = {'iat':time.time()}
            token_dict.update(id)
            headers = {'alg':'HS256'}
            jwt_token = jwt.encode(token_dict,'chenhu0905',algorithm='HS256',headers=headers).decode('ascii')
            Usertoken.objects.update_or_create(user=shop_user(id['id']), defaults={'token': jwt_token})
            return JsonResponse({"code":200,'msg':"登录成功","token":jwt_token,'user_id':id['id']})
        return JsonResponse({"code":400,"msg":"用户不存在"})


# 菜单列表api
class MenuView(APIView):
    def get(self, request, format=None):
        """
        通过APIView实现登录
        """
        data= []
        b=menu.objects.filter(is_delete=0).values('id','menuName')
        for c in list(b):
            id = c.get("id")
            s=submenu.objects.filter(is_delete=0,menu=id).values('id','subName','path')
            c['children'] = list(s)
            data.append(c)
        return JsonResponse({"code":200,"msg":"获取菜单成功",'data':data})

class MyLimitOffsetPagination(LimitOffsetPagination):
    #默认显示的个数
    default_limit = 10
    #当前的位置
    offset_query_param = "offset"
    #通过limit改变默认显示的个数
    limit_query_param = "limit"
    #一页最多显示的个数
    max_limit = 100

#   用户信息api
class UserList(APIView):
    filter_backends = [DjangoFilterBackend]
    filter_fileds = ['fullname']
    def get(self, request,*args,**kwargs):
        """
        通过APIView实现登录
        """
        #获取所有数据
        fullname = request.GET.get("fullname")
        if fullname:
            roles = shop_user.objects.filter(fullname=fullname)
        else:
            roles = shop_user.objects.all()
        #创建分页对象
        pg = MyLimitOffsetPagination()
        #获取分页的数据
        page_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
        #对数据进行序列化
        ser = PagerSerialiser(instance=page_roles,many=True)
        return pg.get_paginated_response(ser.data)


class Run_Script(APIView):

    # filter_backends = [DjangoFilterBackend]
    # filter_fileds = ['page_name','src_name']
    authentication_classes = [AuthenticationSelf,]
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
        c = methodcaller(src_name, **body)(b)
        return JsonResponse(json_dumps_params={'ensure_ascii':False},data={'code': 200,'msg':c,'data':[]})


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