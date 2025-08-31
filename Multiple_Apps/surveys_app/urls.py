from django.urls import path
from . import views

urlpatterns=[
path ('surveys/',views.survey,name='survey'),
path('surveys/new/',views.new_survey,name='new_survey')
]