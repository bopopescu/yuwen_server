# Generated by Django 2.2.4 on 2020-07-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20200704_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='remark',
            field=models.TextField(default='', null=True, verbose_name='备注'),
        ),
    ]
