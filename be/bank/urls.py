from django.urls import path
from bank.views import CardView, CardDetail, BankView, CheckATMCard

urlpatterns = [
    path("api/card/", CardView.as_view()),
    path("api/card/<int:pk>/", CardDetail.as_view()),
    path("api/bank/", BankView.as_view()),
    path("api/checkcard/", CheckATMCard.as_view()),
]
