from django.test import TestCase

from wiki.models import *

class ModelTest(TestCase):
    def test_utc_date(self):
      self.fail(default_now())  