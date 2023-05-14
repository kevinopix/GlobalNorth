from import_export import resources
from services.models import Package


class PackageResource(resources.ModelResource):

    class Meta:
        model = Package