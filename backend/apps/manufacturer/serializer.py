from rest_framework import serializers # type: ignore
from .models import Manufacturer

class ManufacturerSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Manufacturer
    fields = '__all__'