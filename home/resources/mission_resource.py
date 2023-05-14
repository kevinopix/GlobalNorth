from import_export import resources
from home.models import Mission


class MissionResource(resources.ModelResource):

    class Meta:
        model = Mission