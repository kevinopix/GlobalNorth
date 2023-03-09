from import_export import resources
from accounts.models import UserProfile


class UserProfileResource(resources.ModelResource):

    class Meta:
        model = UserProfile