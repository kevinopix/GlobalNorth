from import_export import resources
from services.models import Price


class PackagePriceResource(resources.ModelResource):

    class Meta:
        model = Price