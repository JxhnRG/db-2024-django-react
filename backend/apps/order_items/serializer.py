from rest_framework import serializers # type: ignore
from .models import Order_Items

class Order_itemsSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Order_Items
    fields = '__all__'