from rest_framework.response import Response
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Home(request):
    return Response({
        "status": True,
        "messages": "login success"
    })