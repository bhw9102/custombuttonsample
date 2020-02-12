from django.db import models


class Case(models.Model):
    content = models.CharField(max_length=16, null=True, blank=True, default='default content')