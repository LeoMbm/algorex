
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import ProfileSerializer



@api_view(['POST'])
def create_user(request):
    serializer = ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


