from django.contrib import admin
from django.urls import path
from .views import student_form

urlpatterns = [
    path('student_form/', student_form, name = "form" ),
]