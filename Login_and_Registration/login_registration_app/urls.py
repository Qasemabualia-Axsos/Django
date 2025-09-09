from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('delete',views.delete,name='delete'),
    path('login',views.login,name='login')
]
