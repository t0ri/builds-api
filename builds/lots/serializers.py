from lots.models import Lot
from rest_framework import serializers

# Lot Serializer
class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = '__all__'
