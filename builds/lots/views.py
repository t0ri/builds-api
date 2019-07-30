from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from models import Lot

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_user_lots(request):
    """Get all lots belonging to a user"""
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def post_lot(request):
    """Creates new lot"""
    print(request)
    username = request.data.get("username")
    password = request.data.get("password")
    data = Lot(username, password)
