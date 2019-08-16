from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User


from . import models, serializers


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lots(request, username):
    """Get all lots belonging to a user"""
    author_object = User.objects.get(username=username)
    author_id = author_object.id
    lots = models.Lot.objects.all().filter(author_id=author_id)
    serializer = serializers.LotSerializer(lots, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_lot(request, id):
    """Get specific lot belonging to a user, given lot ID"""
    lot = models.Lot.objects.get(id=id)
    if lot:
        serializer = serializers.LotSerializer(lot)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
@permission_classes((IsAuthenticated,))
def update_lot(request, id):
    """Updates lot, given lot ID"""
    lot = models.Lot.objects.get(id=id)
    serializer = serializers.LotSerializer(lot, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes((IsAuthenticated,))
def delete_lot(request, id):
    """Deletes lot, given lot ID"""
    lot = models.Lot.objects.get(id=id)
    if lot:
        lot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def new_lot(request):
    """Creates new lot"""
    user = request.user
    data = request.data
    data['author_id'] = user.id
    serializer = serializers.LotSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



