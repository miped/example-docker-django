from __future__ import unicode_literals

from django.db import models


class CounterManager(models.Manager):

    def increment(self):
        counter, created = self.get_or_create()
        counter.count += 1
        counter.save()

    def decrement(self):
        counter, created = self.get_or_create()
        counter.count -= 1
        counter.save()


class Counter(models.Model):
    count = models.IntegerField(default=0)

    objects = CounterManager()
