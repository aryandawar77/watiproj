from rest_framework.serializers import Serializer
from rest_framework import serializers

class SumSerializer(Serializer):
  num1 = serializers.IntegerField(required=True)
  num2 = serializers.IntegerField(required=True)