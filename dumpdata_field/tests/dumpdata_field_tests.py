"""Tests for the dumpdata_field command."""
from django.test import TestCase

from .test_app.models import DummyModel
from ..management.commands.dumpdata_field import Command


class DumpdataFieldTestCase(TestCase):
    """Tests for the ``DumpdataField`` management command."""
    longMessage = True

    def test_command(self):
        DummyModel.objects.create(field1=1, field2='foo', field3=True)
        DummyModel.objects.create(field1=2, field2='bar', field3=False)
        command = Command()
        result = command.handle('test_app.DummyModel', fields='field1,field2')
        self.assertEqual(
            result,
            ('[{"field2": "foo", "pk": 1, "field1": 1},'
             ' {"field2": "bar", "pk": 2, "field1": 2}]'),
            msg=('Should return correct JSON string'),
        )
