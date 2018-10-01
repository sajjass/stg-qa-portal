# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import dailystats,sprints

# Register your models here.
admin.site.register(dailystats)
admin.site.register(sprints)