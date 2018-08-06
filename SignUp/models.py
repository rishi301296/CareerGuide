# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    mobile = models.IntegerField(max_length = 12)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length = 6)
    school = models.CharField(max_length = 100)
    stream = models.CharField(max_length = 100)
    entrannce_exam = models.CharField(max_length = 100)
    address = models.TextField()
    father_name = models.CharField(max_length = 100)
    father_mobile = models.IntegerField(max_length = 12)