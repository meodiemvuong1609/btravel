from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.db.models import F
from general.general import convert_response
from account.models import Account, Gender, Address, System, AccountType
from bank.models import Card
from bank.serializers import CardSerializer
from location.serializers import AreaSerializer, ProvinceSerializer, DistrictSerializer, WardSerializer

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ["id", "title", "code"]

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ["id", "title", "code"]


class AccountSerializerAccountType(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "full_name", "avatar", "email", "phone", "is_active", "account_type", "key_account"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

class AccountTypeSerializer(serializers.ModelSerializer):
    account_type_parent__title = serializers.ReadOnlyField(source="account_type_parent.title")
    count_staff = serializers.SerializerMethodField()
    
    class Meta:
        model = AccountType
        fields = ["id", "title", "code", "description", "settings", "account_type_parent", "account_type_parent__title", "system", "user_created", "count_staff", "created_at", "updated_at"]

    def create(self, validated_data):
        account = self.context["request"].user
        validated_data["user_created"] = account
        validated_data["system"] = account.system
        validated_data["code"] = validated_data["account_type_parent"].code 
        validated_data["settings"] = validated_data["account_type_parent"].settings
        return super().create(validated_data)
    
    def get_count_staff(self, instance):
        account_instance = self.context.get("account")
        if not account_instance:
            return None
        account = Account.objects.filter(parent_account=account_instance, is_active=True, account_type=instance)
        return account.count()
    
class AccountTypeDetailSerializer(serializers.ModelSerializer):

    account_type_parent__title = serializers.ReadOnlyField(source="account_type_parent.title")
    count_staff = serializers.SerializerMethodField()

    class Meta:
        model = AccountType
        fields = ["id", "title", "code", "description", "settings", "account_type_parent", "account_type_parent__title", "system", "count_staff", "user_created", "created_at", "updated_at"]

    def get_count_staff(self, instance):
        account_instance = self.context.get("account")
        if not account_instance:
            return None
        account = Account.objects.filter(parent_account=account_instance, is_active=True, account_type=instance)
        return account.count()
    
class AddressSerilaizer(serializers.ModelSerializer):
    area_data = AreaSerializer(source='area', read_only=True)
    province_data = ProvinceSerializer(source='province', read_only=True)
    district_data = DistrictSerializer(source='district', read_only=True)
    ward_data = WardSerializer(source='ward', read_only=True)
    class Meta:
        model = Address
        fields = ["id", "title", "lat", "long", "area", "province", "district", "ward", "settings", "area_data", "province_data", "district_data", "ward_data"]

        extra_kwargs = {
            "area": {"required": False},
            "province": {"required": True},
            "district": {"required": True},
            "ward": {"required": False},
        }
    def create(self, validated_data):
        validated_data["area"] = validated_data["province"].area
        return super().create(validated_data)

class AccountSerializer(serializers.ModelSerializer):
    account_type_data = AccountTypeSerializer(source='account_type', read_only=True)
    gender_data = GenderSerializer(source='gender', read_only=True)
    address_data = AddressSerilaizer(source='address', read_only=True)
    system_data = SystemSerializer(source='system', read_only=True)
    warehouse_data = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = "__all__"

        extra_kwargs = {
            "password": {"write_only": True},
            "full_name": {"required": True},
        }
    def validate(self, attrs):
        if len(attrs["phone"]) < 10:
            raise serializers.ValidationError({"error": "Phone length is too short"})
        if len(attrs["password"]) < 8:
            raise serializers.ValidationError({"error": "Password length is too short"})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data["key_account"] = f"#ACCOUNT{Account.objects.count() + 1}"
        validated_data["password"] = make_password(validated_data["password"])
        validated_data["system"] = self.context["system"]
        validated_data["user_created"] = self.context["user_created"] if "user_created" in self.context else None

        return super().create(validated_data)

class AccountViewSerializer(serializers.ModelSerializer):
    system_data = SystemSerializer(source='system', read_only=True)
    address_data = AddressSerilaizer(source='address', read_only=True)
    class Meta:
        model = Account
        fields = "__all__"

        extra_kwargs = {
            "password": {"write_only": True},
        }
