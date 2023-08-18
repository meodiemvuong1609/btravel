from rest_framework.views import APIView, Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.db.models import Q
from django.db import transaction
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
import generic.swagger_example as swg
from general.general import *
from account.serializers import AccountViewSerializer
from account.models import Account

class AccountLogin(APIView):
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Login',
        operation_description='Login',
        request_body = swg.api_login
    )
    def post(self, request):
        phone = request.data.get("phone", None)
        password = request.data.get("password", None)

        if not phone or not password:
            return Response(convert_response("Required phone, password", 400))
        try:
            account = Account.objects.get(phone=phone)
        except:
            return Response(convert_response("Account not found", 400))
        if not account.check_password(password):
            return Response(convert_response("Invalid password", 400))   
        if account.is_active == False:
            return Response(convert_response("Account not activate", 400))
        token, created = Token.objects.get_or_create(user=account)
        serializer = AccountViewSerializer(account)
        return Response(convert_response("Success", 200, {"token": token.key, "user": serializer.data}))

class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Change Password',
        operation_description="Change Password",
        request_body = swg.api_change_password
    )
    def put(self, request):
        old_password = request.data.get("old_password", None)
        new_password = request.data.get("new_password", None)

        user = request.user
        if not old_password or not new_password:
            return Response(convert_response("Required old_password and new_password", 400))
        if len(new_password) < 8:
            return Response(convert_response("Password length is too short", 400)) 
        if new_password == old_password:
            return Response(convert_response("New_password and Old_password should not be the same", 400))
        account = Account.objects.get(pk=user.id)
        if not check_password(old_password, account.password):
            return Response(convert_response("Old_password is invalid", 400))
        account.set_password(new_password)
        account.save()
        return Response(convert_response("Success", 200))

class ForgotPassword(APIView):
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Send Email',
        operation_description="SEND EMAIL FORGOT PASSWORD",
        request_body = swg.api_forgot_password
    )
    def post(self, request):
        phone = request.data.get("phone", None)
        system_code = request.data.get("system_code", None)

        if not phone or not system_code:
            return Response(convert_response("Required phone and system_code", 400))
        try:
            account = Account.objects.get(phone=phone)
        except:
            return Response(convert_response("Phone not found", 400))
        if account.system.code != system_code:
            return Response(convert_response("You don't permission", 400))
        login(request, account)
        if not account.email:
            return Response(convert_response("Email not found", 404))
        otp = send_otp(email=account.email, template="template_forgot_password.html")
        request.session["otp_forgot"] = otp
        request.session["verified"] = False
        sessionId = {
            "session_key" : request.session._SessionBase__session_key,
            "email" : account.email
        }
        return Response(convert_response("Success", 200, sessionId))

class VerifyEmailForgotPassword(APIView):
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Verify Otp',
        operation_description='VERIFY OTP FORGOT',
        request_body = swg.verify_otp_forgot
    )   
    def post(self, request):
        session_key = request.data.get("session_key", None)
        otp_forgot_input = request.data.get("otp_forgot", None)

        if not session_key or not otp_forgot_input:
            return Response(convert_response("Required session_key and otp_forgot", 400))
        try:
            session = Session.objects.get(session_key=session_key)
            data_decoded = session.get_decoded()
            otp_forgot = data_decoded["otp_forgot"]
            account_id = data_decoded["_auth_user_id"]
            if otp_forgot_input == str(otp_forgot):
                account = Account.objects.get(pk=account_id)
                if account.is_active == False:
                    return Response(convert_response("Account is not active", 400))
                data_decoded["verified"] = True
                session.session_data = SessionStore().encode(data_decoded)
                session.save()
                request.session["verified"] = True
                return Response(convert_response("Success", 200))
            return Response(convert_response("Invalid otp", 400))
        except:
            return Response(convert_response("Invalid session_key", 400))
        
class ResetPassword(APIView):
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Reset Password',
        operation_description='Reset Password',
        request_body = swg.api_reset_password
    ) 
    def post(self, request):
        session_key = request.data.get("session_key", None)
        new_password = request.data.get("new_password", None)
        confirm_password = request.data.get("confirm_password", None)

        if not new_password or not confirm_password :
            return Response(convert_response("Required new_password, confirm_password", 400))
        if len(new_password) < 8:
            return Response(convert_response("Password length is too short", 400))    
        if new_password != confirm_password:
            return Response(convert_response("Required new_password and confirm_password must the same", 400))
        try:
            session = Session.objects.get(session_key=session_key)
            data_decoded = session.get_decoded()
            verified = data_decoded["verified"]
            account_id = data_decoded["_auth_user_id"]
            if new_password != confirm_password:
                return Response(convert_response("New_password and Confirm_password must be the same", 400))
            if verified == True:
                account = Account.objects.get(pk=account_id)
                if account.is_active == False:
                    return Response(convert_response("Account is not active", 400))
                account.set_password(new_password)
                account.save()
                return Response(convert_response("Success", 200))
            return Response(convert_response("Invalid otp", 400))  
        except:
            return Response(convert_response("Invalid session_key", 400))

class ResetOTPView(APIView):
    @swagger_auto_schema(
        tags=["Account"],
        responses=status_response,
        operation_id='Reset OTP',
        operation_description="Reset OTP",
        request_body = swg.api_reset_OTP
    )
    def post(self, request):
        session_key = request.data.get("session_key", None)
        try:
            session = Session.objects.get(session_key=session_key)
        except:
            return Response(convert_response("Invalid session_key", 400))
        data_decoded = session.get_decoded()
        account = Account.objects.get(pk=data_decoded["_auth_user_id"])
        otp = send_otp(email=account.email, template="template_forgot_password.html")
        data_decoded["otp_forgot"] = otp
        session.session_data = SessionStore().encode(data_decoded)
        session.save()
        request.session["otp_forgot"] = otp
        return Response(convert_response("Success", 200))