from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from models import Lot


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lot(request):
    """Get specific lot belonging to a user, given lot ID"""
    data = {'sample_data': 123}
    return Response(data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lots(request):
    """Get all lots belonging to a user"""
    data = {'sample_data': 123}
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def new_lot(request):
    """Creates new lot"""
    print(request)


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def update_lot(request):
    """Updates lot, given lot ID"""
    print(request)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_lot(request):
    """Updates lot, given lot ID"""
    print(request)