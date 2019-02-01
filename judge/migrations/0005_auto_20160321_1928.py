# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0004_problem_num_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='judge.Coder'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='problem',
            name='num_tests',
            field=models.IntegerField(default=1),
        ),
    ]
