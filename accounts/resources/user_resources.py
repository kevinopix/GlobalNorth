from import_export import resources
from accounts.models import User


class UserResorce(resources.ModelResource):

    class Meta:
        model = User