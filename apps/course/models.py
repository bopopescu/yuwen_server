# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

# 课程材料
class Material(models.Model):
    PDF_TYPE, MP4_TYPE, IMG_TYPE, DOC_TYPE, EXCEL_TYPE, URL_TYPE = range(6)

    TYPE_LIST = [
        (PDF_TYPE, 'PDF文档'),
        (MP4_TYPE, '视频mp4'),
        (IMG_TYPE, '图片'),
        (DOC_TYPE, 'DOC文档'),
        (EXCEL_TYPE, 'Excel文档'),
        (URL_TYPE, '链接内容')
    ]

    title = models.CharField(max_length=127, unique=True, verbose_name="名称")
    types = models.PositiveSmallIntegerField(default=0, choices=TYPE_LIST, verbose_name="类型")
    url = models.URLField(default="", verbose_name="地址链接")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"资料"
        verbose_name_plural = verbose_name

# 课程
class Package(models.Model):
    GRADE_ONE, GRADE_TWO, GRADE_THREE, GRADE_FOUR, GRADE_FIVE, GRADE_SIX = range(6)
    GRADE_LIST = [
        (GRADE_ONE, '1年级'),
        (GRADE_TWO, '2年级'),
        (GRADE_ONE, '3年级'),
        (GRADE_ONE, '4年级'),
        (GRADE_ONE, '5年级'),
        (GRADE_ONE, '6年级')
    ]

    title = models.CharField(max_length=127, verbose_name="课程名称", unique=True)
    intro = models.TextField(default="", verbose_name="课程介绍", blank=True)

    count = models.PositiveSmallIntegerField(default=0, verbose_name="课节数", blank=True)

    cover_img = models.URLField(default="", verbose_name="封面图片", blank=True)
    thum_img = models.URLField(default="", verbose_name="缩略图", blank=True)

    grade = models.PositiveSmallIntegerField(default=0, verbose_name="适用年级", choices=GRADE_LIST)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

class Ware(models.Model):
    title = models.CharField(max_length=127, verbose_name="课节名称")
    intro = models.TextField(default="", verbose_name="课节介绍", blank=True)
    package = models.ForeignKey(Package, verbose_name="所属课程", on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0, verbose_name="课序号")

    # 封面图片地址
    cover = models.URLField(default="", verbose_name="封面图片", blank=True)
    thum_img = models.URLField(default="", verbose_name="缩略图", blank=True)

    material = models.ManyToManyField(Material, verbose_name="课节资料")

    def __str__(self):
        return "%s 第%d节课 %s" % (self.package.title, self.index, self.title)

    class Meta:
        verbose_name = "课节"
        verbose_name_plural = verbose_name

        unique_together = ['package', 'title']