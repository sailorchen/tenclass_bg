from django.contrib import admin
from first.models import env_table,src_table,shop_user

# Register your models here.
@admin.register(env_table)
class env_admin(admin.ModelAdmin):
    list_display = ('id','env','shop_label','shop')

@admin.register(src_table)
class env_admin(admin.ModelAdmin):
    list_display = ('id','src_page','src_name','src_desc','src_label','is_delete')

@admin.register(shop_user)
class env_admin(admin.ModelAdmin):
    list_display = ('id','username','password','fullname','mobile','email','status')


# admin.site.register(env_table)