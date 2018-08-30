# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import datetime

class User_Detail(models.Model):
    ############################################################
    #############       Basic Details (5)     ##################
    ############################################################
    
    name = models.CharField(max_length = 100)
    email = models.CharField(primary_key=True, max_length = 100)
    password = models.CharField(max_length = 100)
    mobile = models.IntegerField()
    role = models.CharField(max_length = 50)

    ############################################################
    #############        Extra Details        ##################
    ############################################################
    
    date_of_birth = models.DateField(default = datetime.datetime.today().strftime('%Y-%m-%d'))
    gender = models.CharField(max_length = 6, default = 'NA')
    school = models.CharField(max_length = 100, default = 'NA')
    city = models.CharField(max_length = 30, default = 'NA')
    state = models.CharField(max_length = 30, default = 'NA')
    father_name = models.CharField(max_length = 100, default = 'NA')
    father_mobile = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.email

class User_Authentication(models.Model):
    ############################################################
    #############        Basic Details        ##################
    ############################################################
    
    name = models.CharField(max_length = 100)
    email = models.CharField(primary_key=True, max_length = 100)
    password = models.CharField(max_length = 100)
    mobile = models.IntegerField()

    def __unicode__(self):
        return self.email