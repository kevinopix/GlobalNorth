from import_export import resources
from home.models import Vision


class VisionResource(resources.ModelResource):

    class Meta:
        model = Vision