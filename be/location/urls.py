from django.urls import path
from location.views.location_view import ProvinceView, DistrictView, WardView, AreaView
from location.views.location_json import ProvinceViewJSON, DistrictViewJSON, WardViewJSON
from location.views.load_data import LocationView

urlpatterns = [
    path("api/area/", AreaView.as_view()),
    path("api/province/", ProvinceView.as_view()),
    path("api/district/<int:pk>/", DistrictView.as_view()),
    path("api/ward/<int:pk>/", WardView.as_view()),
    path("api/importlocation/", LocationView.as_view()),
]
