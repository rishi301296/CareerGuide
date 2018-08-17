# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class College(models.Model):
    collegeId = models.CharField(primary_key = True, max_length = 50)
    collegeName = models.CharField(max_length = 100)
    collegeCity = models.CharField(max_length = 100)
    collegeState = models.CharField(max_length = 100)
    totalStudent = models.IntegerField(default=0)
    placedStudent = models.IntegerField(default=0)
    tuitionFee = models.IntegerField(default=0)
