"""Management command that imports certain fields of a model from JSON."""
import json

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = 'file_path'
    help = 'Usage: loaddata_field app_name.ModelName output.json'

    def handle(self, *args, **options):
        app_model = args[0].split('.')
        file_path = args[1]
        f = open(file_path, 'r')
        try:
            json_input = f.read()
        finally:
            f.close()

        dict_input = json.loads(json_input)

        model_type = ContentType.objects.get(
            app_label=app_model[0], model=app_model[1].lower())
        model_class = model_type.model_class()

        count = 0
        for item in dict_input:
            obj = None
            try:
                obj = model_class.objects.get(pk=item['pk'])
            except ObjectDoesNotExist:
                pass
            if obj:
                for key, value in item.items():
                    setattr(obj, key, value)
                obj.save()
                count += 1

        msg = 'Updated {0} objects'.format(count)
        return msg
