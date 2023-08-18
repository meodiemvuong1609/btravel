from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from general.general import *
from location.models import Province, District, Ward, Area
from location.serializers import AreaSerializer, ProvinceSerializer, DistrictSerializer, WardSerializer
# Create your views here.

class AreaView(APIView):

    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get Area',
        operation_description='Get Area',
    )
    def get(self, request):
        area = Area.objects.all().order_by("id")
        serializer = AreaSerializer(area, many=True)
        return Response(convert_response("Success", 200, serializer.data))

class ProvinceView(APIView):

    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get Province',
        operation_description='Filter Province params =["area__code", "area", "area__title"]',
    )
    def get(self, request):
        QUERY_ACCEPT = ["area__code", "area_icontains", "area__title"]
        query_params = request.query_params.dict().copy()
        for key in query_params.copy().keys():
            if key not in QUERY_ACCEPT or key in ["page", "limit"]:
                del query_params[key]
        try:
            province = Province.objects.filter(**query_params)
        except Province.DoesNotExist:
            return Response(convert_response("Province not found", 400))
        serializer = ProvinceSerializer(province, many=True)
        return Response(convert_response("Success", 200, serializer.data))
    
class DistrictView(APIView):

    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get District',
        operation_description='Get District',
    )
    def get(self, request, pk):
        try:
            district = District.objects.filter(province=pk)
        except District.DoesNotExist:
            return Response(convert_response("District not found", 400))
        serializer = DistrictSerializer(district, many=True)
        return Response(convert_response("Success", 200, serializer.data))
    
class WardView(APIView):

    @swagger_auto_schema(
        tags=["Location"],
        responses=status_response,
        operation_id='Get Ward',
        operation_description='Get Ward',
    )
    def get(self, request, pk):
        try:
            ward = Ward.objects.filter(district=pk)
        except Ward.DoesNotExist:
            return Response(convert_response("Ward not found", 400))
        serializer = WardSerializer(ward, many=True)
        return Response(convert_response("Success", 200, serializer.data))