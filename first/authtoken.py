from rest_framework.authentication import BaseAuthentication
from first.models import Usertoken
from rest_framework import exceptions
'''
    自己写认证类方法梳理
    （1）创建认证类
        继承BaseAuthentication    --->>
        1.重写authenticate方法；
        2.authenticate_header方法直接写pass就可以（这个方法必须写）
    （2）authenticate()返回值（三种）
         None ----->>>当前认证不管，等下一个认证来执行
          raise exceptions.AuthenticationFailed('用户认证失败')       # from rest_framework import exceptions
        有返回值元祖形式：（元素1，元素2）      #元素1复制给request.user;  元素2复制给request.auth
    （3）局部使用
         authentication_classes = [BaseAuthentication,]
    （4）全局使用
        #设置全局认证
        REST_FRAMEWORK = {
            "DEFAULT_AUTHENTICATION_CLASSES":['API.utils.auth.Authentication',]
        }
'''

class AuthenticationSelf(BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        token_obj = Usertoken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败-请申请认证')
        return (token_obj.user,token_obj)

    def authenticate_header(self, request):
        pass
