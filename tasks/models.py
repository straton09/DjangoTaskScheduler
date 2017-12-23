# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Task(models.Model):
	task_text = models.CharField(max_length=200)
	exec_datetime = models.DateTimeField(default=timezone.now())
	priority = models.IntegerField(default=0)
	done = models.BooleanField(default=False)