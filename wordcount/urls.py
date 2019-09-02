
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('count/',views.count, name='count'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/',views.resultat, name='result'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]
