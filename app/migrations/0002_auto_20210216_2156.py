# Generated by Django 2.2.2 on 2021-02-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(default=False, max_length=120),
        ),
    ]
