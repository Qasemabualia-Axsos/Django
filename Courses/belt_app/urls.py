from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('login',views.login,name='login'),
    path('add_course',views.add_course,name='add_course'),
    path('delete_page/<int:course_id>',views.delete_page,name='delete_page'),
    path('delete_course/<int:course_id>',views.delete_course,name='delete_course')

]
