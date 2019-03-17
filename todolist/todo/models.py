from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.BooleanField('Complete')
    create_date = models.DateTimeField(default=datetime.now, blank=True)
    edit_date = models.DateTimeField(null=True, blank=True)
    delete_date = models.DateTimeField(null=True, blank=True)
    conclusion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
