from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAdminUser
from django.db import transaction
from general.general import *
from drf_yasg.utils import swagger_auto_schema
import json
from location.models import Area
from location.serializers import AreaSerializer

class LocationView(APIView):
    permission_classes = [IsAdminUser]
    @swagger_auto_schema(auto_schema=None)
    @transaction.atomic
    def post(self, request):
        data = json.loads(open("location/jsondata/data_full.json").read())
        area = Area.objects.all()
        if area.count() > 0:
            return Response(convert_response("Data is exist", 400))
        serializer = AreaSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(convert_response("Success", 200, data))