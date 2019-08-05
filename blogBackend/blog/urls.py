from django.conf.urls import url
from . import views

# 注册上一级的路由地址并添加
urlpatterns = [
    url(r'api/hello', views.hello),
]
