from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.models import WheelSpecification
from api.serializers import WheelSpecificationSerializer


class WheelSpecificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = WheelSpecification.objects.all()
    serializer_class = WheelSpecificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
