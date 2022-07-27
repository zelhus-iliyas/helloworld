
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    date = datetime.now().strftime("%Y-%m-%d")
    message = "Yo "
    return Response(data=message + date, status=status.HTTP_200_OK)
