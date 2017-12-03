# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from .models import Counter


class CounterTest(TestCase):

    def test_increment(self):
        Counter.objects.increment()
        c = Counter.objects.first()
        self.assertEqual(c.count, 1)

        Counter.objects.increment()
        c = Counter.objects.first()
        self.assertEqual(c.count, 2)

    def test_decrement(self):
        Counter.objects.decrement()
        c = Counter.objects.first()
        self.assertEqual(c.count, -1)

        Counter.objects.decrement()
        c = Counter.objects.first()
        self.assertEqual(c.count, -2)
