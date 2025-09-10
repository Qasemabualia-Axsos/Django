from django.urls import path,include
from . import views

urlpatterns = [
    path('shows/',views.shows,name='shows'),
    path('shows/new/', views.index,name='index'),
    path('shows/<int:num>/',views.action_show,name='action_show'),
    path('shows/<int:num>/edit/',views.action_edit,name="action_edit"),
    path('shows/<int:num>/update/',views.update,name='update'),
    path('shows/<int:num>/destroy/',views.delete,name='delete')
]
