# Generated by Django 2.2.4 on 2020-07-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0003_manager_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='对应邮箱'),
        ),
    ]