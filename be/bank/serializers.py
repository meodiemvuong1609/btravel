from rest_framework import serializers
from general.general import *
from bank.models import Card, CardType, Bank

class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = ["id", "title", "code", "short_name", "img_url", "bin", "swiftCode"]

class CardTypeSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = CardType
        fields = ["id", "title", "code"]

class CardSerializer(serializers.ModelSerializer):
    bank_data = BankSerializer(source='bank', read_only=True)
    card_type_data = CardTypeSerializer(source='card_type', read_only=True)

    class Meta:
        model = Card
        fields = ["id", "full_name", "card_number", "status", "qrcode", "expriry_date", "cvv", "card_type", "bank", "account", "bank_data", "card_type_data"]
        
    def create(self, validated_data):
        account = self.context["account"] if "account" in self.context else None
        validated_data["account"] = self.context["request"].user if "request" in self.context else account
        bank = validated_data["bank"]
        transferType = "INHOUSE" if bank.code == "MB" else "NAPAS"
        code, response = lookup_card(bank.bin, validated_data["card_number"], transferType)
        if code != 200:
            raise serializers.ValidationError(convert_response(response, code, transferType))
        if account:
            validated_data["account"] = account
        return super().create(validated_data)