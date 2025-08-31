from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('play_again/',views.play_again,name='play_again')
]
