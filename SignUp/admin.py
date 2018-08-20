# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User_Authentication, User_Detail

# Register your models here.
admin.site.register(User_Detail)
admin.site.register(User_Authentication)