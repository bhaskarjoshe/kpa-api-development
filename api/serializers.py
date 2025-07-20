from rest_framework import serializers

from .models import WheelSpecification


class WheelSpecificationSerializer(serializers.Serializer):
    class Meta:
        model = WheelSpecification
        fields = "__all__"
