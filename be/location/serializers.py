from rest_framework import serializers
from location.models import Province, District, Ward, Area

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = ["id", "title", "code"]
    
    def create(self, validated_data):
        ward = super().create(validated_data)
        return ward

class DistrictSerializer(serializers.ModelSerializer):
    wards = serializers.ListField(write_only=True, required=False)
    class Meta:
        model = District
        fields = ["id", "title", "code", "wards"]
    
    def create(self, validated_data):
        wards = validated_data.pop("wards", None)
        validated_data["code"] = (str(int(float(validated_data["code"])))).zfill(2)
        district = super().create(validated_data)
        if wards:
            serializer_ward = WardSerializer(data=wards, many=True)
            serializer_ward.is_valid(raise_exception=True)
            serializer_ward.save(district=district)
        return district

class ProvinceSerializer(serializers.ModelSerializer):  
    district = serializers.ListField(write_only=True)
    class Meta:
        model = Province
        fields = ["id", "title", "code", "district"]
    
    def create(self, validated_data):
        district = validated_data.pop("district")
        province = super().create(validated_data)

        serializer_district = DistrictSerializer(data=district, many=True)
        serializer_district.is_valid(raise_exception=True)
        serializer_district.save(province=province)

        return province



class AreaSerializer(serializers.ModelSerializer):
    province = serializers.ListField(write_only=True)
    class Meta:
        model = Area
        fields = ["id", "title", "code", "province"]
    
    def create(self, validated_data):
        province = validated_data.pop("province")
        area = super().create(validated_data)
        serializer_province = ProvinceSerializer(data=province, many=True)
        serializer_province.is_valid(raise_exception=True)
        serializer_province.save(area=area)
        return area




