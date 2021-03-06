# Generated by Django 2.2.4 on 2020-06-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='名称')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='电话')),
                ('head', models.URLField(blank=True, default='', verbose_name='头像')),
                ('openid', models.CharField(blank=True, default='', max_length=64, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, default='', max_length=64, verbose_name='unionid')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '联系人',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='名称')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='电话')),
                ('head', models.URLField(blank=True, default='', verbose_name='头像')),
                ('openid', models.CharField(blank=True, default='', max_length=64, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, default='', max_length=64, verbose_name='unionid')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '管理员',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='名称')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='电话')),
                ('head', models.URLField(blank=True, default='', verbose_name='头像')),
                ('openid', models.CharField(blank=True, default='', max_length=64, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, default='', max_length=64, verbose_name='unionid')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '学生',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, verbose_name='名称')),
                ('phone', models.CharField(max_length=64, unique=True, verbose_name='电话')),
                ('head', models.URLField(blank=True, default='', verbose_name='头像')),
                ('openid', models.CharField(blank=True, default='', max_length=64, verbose_name='openid')),
                ('unionid', models.CharField(blank=True, default='', max_length=64, verbose_name='unionid')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '教师',
            },
        ),
    ]
