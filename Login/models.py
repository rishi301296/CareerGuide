# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Current_User(models.Model):
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)