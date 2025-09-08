from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('authors/',views.authors,name='authors'),
    path('add_book/',views.add_book,name='add_book'),
    path('add_author/',views.add_author,name='add_author'),
    path('books/<int:num>/',views.display_book,name='display_book'),
    path('authors/<int:num>/',views.display_author,name='display_author')

]