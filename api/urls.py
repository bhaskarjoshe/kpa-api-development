from django.urls import path

from api.views import BogieChecksheetView
from api.views import WheelSpecificationListCreateAPIView

urlpatterns = [
    path(
        "api/form_data/wheel-specifications",
        WheelSpecificationListCreateAPIView.as_view(),
        name="wheel-specification-list-create",
    ),
    path(
        "api/forms/bogie-checksheet",
        BogieChecksheetView.as_view(),
        name="bogie-checksheet",
    ),
]
