from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Packs(models.Model):
    number = models.IntegerField(verbose_name=u'Number of pack')


