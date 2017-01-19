# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ShopInfo(models.Model):
    shop_id = models.BigIntegerField(
        null=True, blank=True, unique=True, verbose_name=u'商家id')
    city_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'市名')
    location_id = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'所在位置编号，位置接近的商家具有相同的编号')
    per_pay = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'人均消费（数值越大消费越高）')
    score = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'评分（数值越大评分越高）')
    comment_cnt = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'评论数（数值越大评论数越多）')
    shop_level = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'门店等级（数值越大门店等级越高）')
    cate_1_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'一级品类名称')
    cate_2_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'二级分类名称')
    cate_3_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'三级分类名称')

    class Meta:
        app_label = 'base'
        verbose_name_plural = u'商家特征数据'


class UserPay(models.Model):
    user_id = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'用户id')
    shop_id = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'商家id')
    time_stamp = models.DateTimeField(
        null=True, blank=True, verbose_name=u'支付时间')

    class Meta:
        app_label = 'base'
        verbose_name_plural = u'用户支付行为'


class UserView(models.Model):
    user_id = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'用户id')
    shop_id = models.BigIntegerField(
        null=True, blank=True, verbose_name=u'商家id')
    time_stamp = models.DateTimeField(
        null=True, blank=True, verbose_name=u'浏览时间')

    class Meta:
        app_label = 'base'
        verbose_name_plural = u'用户浏览行为'


class Prediction(models.Model):
    day_1 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第1天的预测值')
    day_2 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第2天的预测值')
    day_3 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第3天的预测值')
    day_4 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第4天的预测值')
    day_5 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第5天的预测值')
    day_6 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第6天的预测值')
    day_7 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第7天的预测值')
    day_8 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第8天的预测值')
    day_9 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第9天的预测值')
    day_10 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第10天的预测值')
    day_11 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第11天的预测值')
    day_12 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第12天的预测值')
    day_13 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第13天的预测值')
    day_14 = models.CharField(
        max_length=255, null=True, blank=True, verbose_name=u'第14天的预测值')

    shop = models.ForeignKey(
        'base.ShopInfo',
        blank=True,
        null=True,
        verbose_name=u'商家'
    )

    class Meta:
        app_label = 'base'
        verbose_name_plural = u'用户浏览行为'

