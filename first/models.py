from django.db import models

# Create your models here.


#用户表
class shop_user(models.Model):

    username = models.CharField(max_length=20,verbose_name="用户名")
    fullname = models.CharField(max_length=60,verbose_name="姓名")
    password = models.CharField(max_length=20,verbose_name="密码")
    mobile = models.CharField(max_length=20,verbose_name="手机号",default='1')
    email = models.CharField(max_length=20,verbose_name="邮箱",default='2')
    status = models.IntegerField(verbose_name="状态:1正常 0不正常",default=1)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name


class env_table(models.Model):

    env = models.CharField(max_length=20,verbose_name="环境")
    shop_label = models.CharField(max_length=20,verbose_name="店铺名称")
    shop = models.CharField(max_length=20,verbose_name="店铺id")
    req_url = models.CharField(max_length=50,verbose_name="请求域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "环境表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.env

class src_table(models.Model):

    src_page = models.CharField(max_length=50,verbose_name='脚本页面名称')
    src_name = models.CharField(max_length=200,verbose_name="脚本名称")
    src_desc = models.CharField(max_length=1000,verbose_name="脚本描述")
    src_label = models.CharField(max_length=200,verbose_name='脚本显示')
    is_delete = models.IntegerField(default=0,verbose_name="是否删除：0-未删 1-已删")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "脚本对应关系表"
        verbose_name_plural = verbose_name

class menu(models.Model):

    menuName = models.CharField(max_length=50,verbose_name='菜单名')
    is_delete = models.IntegerField(default=0,verbose_name="是否删除：0-未删 1-已删")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "一级菜单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.menuName

class submenu(models.Model):

    menu = models.ForeignKey('menu',on_delete=models.CASCADE,verbose_name='父菜单id',related_name='submenu')
    subName = models.CharField(max_length=50,verbose_name='子菜单名')
    path = models.CharField(max_length=50, verbose_name='子页面路由')
    is_delete = models.IntegerField(default=0,verbose_name="是否删除：0-未删 1-已删")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = "子菜单"
        verbose_name_plural = verbose_name