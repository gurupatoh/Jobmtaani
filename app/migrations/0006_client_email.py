# Generated by Django 2.2.2 on 2021-02-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210217_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default='patrickn0023@gmail.com', max_length=254, unique=True),
        ),
    ]