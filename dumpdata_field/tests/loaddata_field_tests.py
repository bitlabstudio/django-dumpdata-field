"""Tests for the loaddata_field command."""
import tempfile

from django.test import TestCase

from .test_app.models import DummyModel
from ..management.commands.loaddata_field import Command


class LoaddataFieldTestCase(TestCase):
    """Tests for the ``DumpdataField`` management command."""
    longMessage = True

    def test_command(self):
        DummyModel.objects.create(field1=3, field2='foobar', field3=True)
        DummyModel.objects.create(field1=4, field2='barfoo', field3=False)
        f = tempfile.NamedTemporaryFile(delete=False)
        f.write('[{"field2": "foo", "pk": 1, "field1": 1}, {"field2": "bar", "pk": 666, "field1": 2}]')  # NOQA
        f.close()
        command = Command()
        result = command.handle('test_app.DummyModel', f.name)
        obj = DummyModel.objects.get(pk=1)
        self.assertEqual(obj.field1, 1, msg=('Should have changed the field'))
        self.assertEqual(result, 'Updated 1 objects', msg=(
            'Should return the update count'))
