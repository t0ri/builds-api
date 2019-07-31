from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from . import models


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lots(request):
    """Get all lots belonging to a user"""
    pass


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lot(request, id):
    """Get specific lot belonging to a user, given lot ID"""
    pass


@api_view(["PUT"])
@permission_classes((IsAuthenticated,))
def update_lot(request, id):
    """Updates lot, given lot ID"""
    pass


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_lot(request, id):
    """Deletes lot, given lot ID"""
    pass


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def new_lot(request):
    """Creates new lot"""
    pass





