from django.db import models

# Create your models here.


#用户表
class shop_user(models.Model):

    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    fullname = models.CharField(max_length=64, null=True, verbose_name='中文名')

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