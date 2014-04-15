"""Dummy models for the tests."""
from django.db import models


class DummyModel(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=128)
    field3 = models.BooleanField()
