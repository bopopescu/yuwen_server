# Generated by Django 2.2.4 on 2020-06-30 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, unique=True, verbose_name='课包名称')),
                ('intro', models.TextField(blank=True, default='', verbose_name='课程介绍')),
                ('count', models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='课节数')),
                ('cover_img', models.URLField(blank=True, default='', verbose_name='封面图片')),
                ('thum_img', models.URLField(blank=True, default='', verbose_name='缩略图')),
                ('grade', models.PositiveSmallIntegerField(choices=[(0, '1年级'), (1, '2年级'), (0, '3年级'), (0, '4年级'), (0, '5年级'), (0, '6年级')], default=0, verbose_name='适用年级')),
                ('is_online', models.BooleanField(blank=True, default=True, verbose_name='是否上线')),
            ],
            options={
                'verbose_name': '课程',
            },
        ),
    ]
