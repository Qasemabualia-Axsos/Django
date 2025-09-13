from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home', views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('post_msg',views.post_msg,name='post_msg'),
    path('wall/',views.wall,name='wall'),
    path('post_comment',views.post_comment,name='post_comment'),
]
