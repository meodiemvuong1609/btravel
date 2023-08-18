from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
import generic.swagger_example as swg
from general.general import *
from account.serializers import  AccountTypeSerializer, AccountTypeDetailSerializer
from account.models import AccountType

class AccountTypeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Account Type"],
        responses=status_response,
        operation_id='Get AccountType',
        operation_description='Filter AccountType params =["title__icontains", "system__code", "code", "account_type_parent", "user_created", "account_type_parent__isnull"]'
    )
    def get(self, request):
        QUERY_ACCEPT = ["title__icontains", "system__code", "code", "account_type_parent", "user_created", "account_type_parent__isnull"]
        BOOL_ACCEPT = ["account_type_parent__isnull"]
        query_params = request.query_params.dict().copy()
        for key in query_params.copy().keys():
            if key not in QUERY_ACCEPT or key in ["page", "limit"]:
                del query_params[key]
            if key in BOOL_ACCEPT:
                if query_params[key] == "true":
                    query_params[key] = True
                elif query_params[key] == "false":
                    query_params[key] = False
        account_type = AccountType.objects.filter(Q(user_created=request.user) | Q(system__code="ADMIN") | Q(system__code="NPT"), **query_params).order_by("-id")
        count = account_type.count()
        account_type = Paginate(account_type, request.GET)
        serializer = AccountTypeSerializer(account_type, many=True, context={"account": request.user})
        return Response(convert_response("Success", 200, serializer.data, count=count))
    
    @swagger_auto_schema(
        tags=["Account Type"],
        responses=status_response,
        operation_id="Create AccountType",
        operation_description='post_AccountType',
        request_body=swg.post_accounttype
    )
    def post(self, request):
        serializer = AccountTypeSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(convert_response("Invalids Params", 400))
        serializer.save()
        return Response(convert_response("Success", 200, serializer.data))

class AccountTypeDetail(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Account Type"],
        responses=status_response,
        operation_id='Get Detail Account Type',
        operation_description='Get detail Account Type',
    )
    def get(self, request, pk):
        try:
            account_type = AccountType.objects.get(Q(user_created=request.user, pk=pk) | Q(system__code='ADMIN', pk=pk))
        except:
            return Response(convert_response("Not found", 400))
        serializer = AccountTypeDetailSerializer(account_type, context={"account": request.user})
        return Response(convert_response("Success", 200, serializer.data))

    @swagger_auto_schema(
        tags=["Account Type"],
        responses=status_response,
        operation_id="Update Account Type",
        operation_description='put_detail_accounttype',
        request_body = swg.put_detail_accounttype
    )
    @transaction.atomic
    def put(self, request, pk):
        try:
            account_type = AccountType.objects.get(user_created=request.user, pk=pk)
        except:
            return Response(convert_response("Not found", 400))
        serializer = AccountTypeDetailSerializer(account_type, request.data, context={"account": request.user})
        if not serializer.is_valid():
            return Response(convert_response("Invalids params", 400))
        serializer.save()
        return Response(convert_response("Success", 200, serializer.data))
    
    @swagger_auto_schema(
        tags=["Account Type"],
        responses=status_response,
        operation_id='Delete Account Type',
        operation_description='Delete Account Type',
    )
    @transaction.atomic
    def delete(self, request, pk):
        try:
            account_type = AccountType.objects.get(user_created=request.user, pk=pk)
        except:
            return Response(convert_response("Not found", 400))
        account_type.delete()
        return Response(convert_response("Success", 200))