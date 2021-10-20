from django.db import models

# Create your models here.

class Register(models.Model):
    
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=154)
    phone = models.CharField(max_length=11)
    number = models.IntegerField()
    
    GENDER = (
        ("1", "Female"),
        ("2", "Male"),
        ("3", "Other"),
        ("4", "Prefer Not Say"),
    )
    gender = models.CharField(max_length = 50, choices=GENDER)
    
    PATH = (
        ("1", "Full Stack Developer"),
        ("2", "Data Science"),
        ("3", "AWS")
    )

    path = models.CharField(max_length = 50, choices=PATH)