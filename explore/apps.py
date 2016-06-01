from django.apps import AppConfig


# TODO: loaded two times (not a problem and may not happen in production) 
# see http://stackoverflow.com/a/16111968 
class ExploreMdcsConfig(AppConfig):
    name = 'explore'
    verbose_name = "explore"

    def ready(self):
        from mgi.models import XMLdata
        XMLdata.initIndexes()

