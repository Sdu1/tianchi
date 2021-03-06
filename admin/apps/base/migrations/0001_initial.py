# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-19 01:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c1\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c2\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c3\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c4\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_5', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c5\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_6', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c6\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_7', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c7\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_8', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c8\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_9', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c9\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_10', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c10\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_11', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c11\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_12', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c12\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_13', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c13\u5929\u7684\u9884\u6d4b\u503c')),
                ('day_14', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u7b2c14\u5929\u7684\u9884\u6d4b\u503c')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u6d4f\u89c8\u884c\u4e3a',
            },
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.BigIntegerField(blank=True, null=True, unique=True, verbose_name='\u5546\u5bb6id')),
                ('city_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u5e02\u540d')),
                ('location_id', models.BigIntegerField(blank=True, null=True, verbose_name='\u6240\u5728\u4f4d\u7f6e\u7f16\u53f7\uff0c\u4f4d\u7f6e\u63a5\u8fd1\u7684\u5546\u5bb6\u5177\u6709\u76f8\u540c\u7684\u7f16\u53f7')),
                ('per_pay', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4eba\u5747\u6d88\u8d39\uff08\u6570\u503c\u8d8a\u5927\u6d88\u8d39\u8d8a\u9ad8\uff09')),
                ('score', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u8bc4\u5206\uff08\u6570\u503c\u8d8a\u5927\u8bc4\u5206\u8d8a\u9ad8\uff09')),
                ('comment_cnt', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u8bc4\u8bba\u6570\uff08\u6570\u503c\u8d8a\u5927\u8bc4\u8bba\u6570\u8d8a\u591a\uff09')),
                ('shop_level', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u95e8\u5e97\u7b49\u7ea7\uff08\u6570\u503c\u8d8a\u5927\u95e8\u5e97\u7b49\u7ea7\u8d8a\u9ad8\uff09')),
                ('cate_1_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e00\u7ea7\u54c1\u7c7b\u540d\u79f0')),
                ('cate_2_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e8c\u7ea7\u5206\u7c7b\u540d\u79f0')),
                ('cate_3_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e09\u7ea7\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'verbose_name_plural': '\u5546\u5bb6\u7279\u5f81\u6570\u636e',
            },
        ),
        migrations.CreateModel(
            name='UserPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='\u7528\u6237id')),
                ('shop_id', models.BigIntegerField(blank=True, null=True, verbose_name='\u5546\u5bb6id')),
                ('time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='\u652f\u4ed8\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u652f\u4ed8\u884c\u4e3a',
            },
        ),
        migrations.CreateModel(
            name='UserView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(blank=True, null=True, verbose_name='\u7528\u6237id')),
                ('shop_id', models.BigIntegerField(blank=True, null=True, verbose_name='\u5546\u5bb6id')),
                ('time_stamp', models.DateTimeField(blank=True, null=True, verbose_name='\u6d4f\u89c8\u65f6\u95f4')),
            ],
            options={
                'verbose_name_plural': '\u7528\u6237\u6d4f\u89c8\u884c\u4e3a',
            },
        ),
        migrations.AddField(
            model_name='prediction',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ShopInfo', verbose_name='\u5546\u5bb6'),
        ),
    ]
