from django.urls import path
from account.views.account_view import AccountLogin, ChangePassword, ForgotPassword, VerifyEmailForgotPassword, ResetPassword, ResetOTPView
from account.views.address_view import AddressDetail
from account.views.account_type import AccountTypeView, AccountTypeDetail
from account.views.gender_view import GenderView



urlpatterns = [
    path("api/login/", AccountLogin.as_view()),
    path("api/changepassword/", ChangePassword.as_view()),
    path("api/forgot_password/", ForgotPassword.as_view()),
    path("api/verify_forgot/", VerifyEmailForgotPassword.as_view()),
    path("api/resetpassword/", ResetPassword.as_view()),
    path("api/reset_otp/", ResetOTPView.as_view()),
    path("api/address/<int:pk>/", AddressDetail.as_view()),
    path("api/accounttype/", AccountTypeView.as_view()),
    path("api/accounttype/<int:pk>/", AccountTypeDetail.as_view()),
    path("api/gender/", GenderView.as_view())
]