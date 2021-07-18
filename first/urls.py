from django.conf.urls import url
from first import views

#路由配置
urlpatterns = [
    url('login',views.LoginView.as_view(),name='login'),
    url('menus', views.MenuView.as_view(),name='menus'),
    url('userlist', views.UserList.as_view()),
    url('run_src', views.Run_Script.as_view(),name='run'),
    url('shop_list', views.list_shop.as_view()),
    url('src_info', views.src_info.as_view()),
]