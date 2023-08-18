from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from general.general import *
from drf_yasg.utils import swagger_auto_schema
from location.subdivisions import subdivision
# Create your views here.

class ProvinceViewJSON(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get Province',
        operation_description='Get Province',
    )

    def get(self, request):
        province = subdivision.json_province
        list_province = list(province.values())
        return Response(convert_response("Success", 200, list_province))
    
class DistrictViewJSON(APIView):
    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get District',
        operation_description='Get District',
    )
    def get(self, request, code):
        district = subdivision.district(province_id=code)
        return Response(convert_response("Success", 200, district))
    
class WardViewJSON(APIView):
    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get Ward',
        operation_description='Get Ward',
    )
    def get(self, request, code):
        ward = subdivision.ward(district_id=code)
        return Response(convert_response("Success", 200, ward))
