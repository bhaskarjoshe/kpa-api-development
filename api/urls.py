from django.urls import path

from api.views import WheelSpecificationListCreateAPIView

urlpatterns = [
    path(
        "api/form_data/wheel-specifications",
        WheelSpecificationListCreateAPIView.as_view(),
        name="wheel-specification-list-create",
    ),
]
