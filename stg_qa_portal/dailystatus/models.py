# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sprints(models.Model):
    latest_sprint = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.latest_sprint


class dailystats(models.Model):
    sprint = models.ForeignKey(sprints, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    story_id = models.CharField(max_length=30)
    project = models.CharField(max_length=30)
    Task = models.CharField(max_length=250)
    Description = models.TextField(max_length=5000)
    defects_filed = models.CharField(max_length=250, blank=True)
    defects_verified = models.CharField(max_length=250, blank=True)
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return self.Task