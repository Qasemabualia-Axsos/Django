from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('success/',views.success,name='success'),
    path('delete/',views.delete,name='delete'),
    path('add_book',views.add_book,name='add_book'),
    path('books/<int:book_id>/',views.display_book,name='display_book'),
    path('edit/<int:book_id>/',views.edit_book,name='edit_book'),
    path('delete_book/<int:book_id>/',views.delete_book,name='delete_book'),
    path('books/<int:book_id>/favorite/', views.add_fav, name="add_fav"),
    path('books/<int:book_id>/unfavorite',views.remove_fav,name='remove_fav')


]
