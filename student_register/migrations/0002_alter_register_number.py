# Generated by Django 3.2.8 on 2021-10-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='number',
            field=models.CharField(max_length=11),
        ),
    ]
