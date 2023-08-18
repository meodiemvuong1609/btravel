from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
import generic.swagger_example as swg
from general.general import *
from account.models import Address
from account.serializers import AddressSerilaizer

class AddressDetail(APIView):
    permission_classes =[IsAuthenticated]

    @swagger_auto_schema(
        tags=["Address"],
        responses=status_response,
        operation_id='Update Address',
        operation_description='put_detail_address',
        request_body = swg.put_detail_address
    )
    @transaction.atomic
    def put(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response(convert_response("Not found", 400))
        serializer = AddressSerilaizer(address, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(convert_response("Success", 200, serializer.data))
    
    @swagger_auto_schema(
        tags=["Address"],
        responses=status_response,
        operation_id='Delete address',
        operation_description='Delete address',
    )
    @transaction.atomic
    def delete(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response(convert_response("Not found", 400))
        address.delete()
        return Response(convert_response("Success", 200))