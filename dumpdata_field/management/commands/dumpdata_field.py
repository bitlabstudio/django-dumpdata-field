"""Management command that exports certain fields of a model to JSON."""
import json
from optparse import make_option

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
            '-f', '--fields',
            help='Comma separated list of field names',
        ),
    )
    args = 'file_path'
    help = 'Usage: dumpdata_field app_name.ModelName --fields=field1,field2'

    def values_query_set_to_dict(self, vqs):
        return [item for item in vqs]

    def handle(self, *args, **options):
        app_model = args[0].split('.')
        fields = options['fields'].split(',')
        if not 'pk' in fields:
            fields.insert(0, 'pk')

        model_type = ContentType.objects.get(
            app_label=app_model[0], model=app_model[1].lower())

        result = model_type.model_class().objects.all().values(*fields)
        result = self.values_query_set_to_dict(result)
        result = json.dumps(result)
        return result
