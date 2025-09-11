from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('destroy_session/',views.destroy,name='destroy_session'),
    path('increment_by_2/',views.increment_by_2,name='incremet'),
    path('increment_by_user/',views.incremet_by_user,name='incremet_by_user')
]
