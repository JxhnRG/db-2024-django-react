from rest_framework import generics, status # type: ignore
from rest_framework.response import Response # type: ignore

from .models import Manufacturer
from .serializer import ManufacturerSerializer # type: ignore

class ListCreateManufacturer(generics.ListAPIView):
  queryset = Manufacturer.objects.all()
  serializer_class = ManufacturerSerializer
  
  def post(self, request, *args, **kwargs):
    data= request.data
    serr = ManufacturerSerializer(data=data)
    if (serr.is_valid()):
      serr.save()
      return Response(serr.validated_data, status=status.HTTP_200_OK)  
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
    