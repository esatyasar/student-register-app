from django.contrib import admin
from django.urls import path
from .views import student_form, student_list

urlpatterns = [
    path('student_form/', student_form, name = "form" ),
    path('', student_list, name = "list" ),
]