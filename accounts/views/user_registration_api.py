from rest_framework.views import APIView
from rest_framework.response import Response
# from accounts.serializers import UserAPISerializer

class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = UserAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)