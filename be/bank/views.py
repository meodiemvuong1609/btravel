from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
import generic.swagger_example as swg
from general.general import *
from bank.models import Card, Bank
from bank.serializers import CardSerializer, BankSerializer
from account.models import Account

class CardView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Card"],
        responses=status_response,
        operation_id='Card',
        operation_description='Filter card params =["title__icontains", "card_number__icontains", "status__icontains", "card_type", "bank", "account"]'
    )
    def get(self, request):
        QUERY_ACCEPT = ["title__icontains", "card_number__icontains", "status__icontains", "card_type", "bank", "account"]
        query_params = request.query_params.dict().copy()
        for key in query_params.copy().keys():
            if key not in QUERY_ACCEPT or key in ["page", "limit"]:
                del query_params[key]
        card = Card.objects.filter(account=request.user, **query_params).order_by("-id")
        count = card.count()
        card = Paginate(card, request.GET)
        serializer = CardSerializer(card, many=True)
        return Response(convert_response("Success", 200, serializer.data, count=count))
    
    @swagger_auto_schema(
        tags=["Card"],
        responses=status_response,
        operation_id='Post Card',
        operation_description='post_card',
        request_body=swg.post_card
    )
    @transaction.atomic
    def post(self, request):
        account = request.data.get("account")
        if account is not None:
            try:
                account_instance = Account.objects.get(id=account)
            except Account.DoesNotExist:
                return Response(convert_response("Not found account", 400))
        else:
            account_instance = None 
        serializer = CardSerializer(data=request.data, context={'request': request, 'account': account_instance})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(convert_response("Success", 200, serializer.data))
    
class CardDetail(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Card"],
        responses=status_response,
        operation_id='Get detail card',
        operation_description='Get detail card',
    )
    def get(self, request, pk):
        try:
            card = Card.objects.get(account=request.user, pk=pk)
        except:
            return Response(convert_response("Error", 400))
        serializer = CardSerializer(card)
        return Response(convert_response("Success", 200, serializer.data))
    
    @swagger_auto_schema(
        tags=["Card"],
        responses=status_response,
        operation_id='Put Card',
        operation_description='put_detail_card',
        request_body = swg.put_detail_card
    )
    @transaction.atomic
    def put(self, request, pk):
        try:
            card = Card.objects.get(account=request.user, pk=pk)
        except:
            return Response(convert_response("Error", 400))
        serializer = CardSerializer(card, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(convert_response("Success", 200, serializer.data))
    
    @swagger_auto_schema(
        tags=["Card"],
        responses=status_response,
        operation_id='Delete card',
        operation_description='Delete card',
    )
    @transaction.atomic
    def delete(self, request, pk):
        try:
            card = Card.objects.get(account=request.user, pk=pk)
        except Card.DoesNotExist:
            return Response(convert_response("Error", 400))
        card.delete()
        return Response(convert_response("Success", 200))

    
class BankView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Bank"],
        responses=status_response,
        operation_id='Bank',
        operation_description='Bank',
    )
    def get(self, request):
        QUERY_ACCEPT = ["title__icontains", "code__icontains", "short_name__icontains"]
        query_params = request.query_params.dict().copy()
        for key in query_params.copy().keys():
            if key not in QUERY_ACCEPT or key in ["page", "limit"]:
                del query_params[key]
        bank = Bank.objects.filter(**query_params).order_by("-id")
        count = bank.count()
        bank = Paginate(bank, request.GET)
        serializer = BankSerializer(bank, many=True)
        return Response(convert_response("Success", 200, serializer.data, count=count))
    

class CheckATMCard(APIView):

    @swagger_auto_schema(
        tags=["Bank"],
        responses=status_response,
        operation_id='Check ATM Card',
        operation_description='Check ATM Card',
        request_body=swg.check_atm_card
    )

    def post(self, request):
        bin = request.data.get("bin", None)
        accountNumber = request.data.get("accountNumber", None)
        transferType = request.data.get("transferType", None)
        if not bin or not accountNumber or not transferType:
            return Response(convert_response("Required bin, accountNumber, transferType", 400))
        code, message = lookup_card(bin, accountNumber, transferType)
        if code == 200:
            return Response(convert_response("Success", 200, message))
        else:
            return Response(convert_response(message, 400))