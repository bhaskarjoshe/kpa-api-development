from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from api.models import BogieChecksheet
from api.models import WheelSpecification
from api.serializers import BogieChecksheetSerializer
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


class BogieChecksheetView(generics.CreateAPIView):
    queryset = BogieChecksheet.objects.all()
    serializer_class = BogieChecksheetSerializer

    def post(self, request, *args, **kwargs):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Bogie checksheet submitted successfully.",
                    "data": {
                        "formNumber": serializer.data.get("formNumber", ""),
                        "inspectionBy": serializer.data.get("inspectionBy", ""),
                        "inspectionDate": serializer.data.get("inspectionDate", ""),
                        "status": serializer.data.get("status", "Saved"),
                    },
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "message": "Validation error",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
