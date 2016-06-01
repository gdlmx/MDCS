from django.apps import AppConfig



# TODO: loaded two times (not a problem and may not happen in production) 
# see http://stackoverflow.com/a/16111968 
class ExporterConfig(AppConfig):
    name = 'exporter'
    verbose_name = "Exporter"

    def ready(self):
        from exporter import discover
        discover.discover_exporter()
