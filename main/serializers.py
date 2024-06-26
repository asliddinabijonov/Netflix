from rest_framework import serializers
from .models import *


class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    ism = serializers.CharField(max_length=255)
    davlat = serializers.CharField(max_length=50)
    jins = serializers.CharField(max_length=10)
    t_yil = serializers.DateField(required=False)


class KinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'  # ('id', 'nom', 'janr'..)

    def validate_yil(self, value):
        if int(value) < 1800:
            raise serializers.ValidationError("Kino ushbu yilga tegishli bo'la olmaydi!")
        return value


# Aktyor ismi 3 tadan kam bo'lgan holat uchun validation yozamiz
# Aktyorda jins ustuni erkak yoki ayol bo'lsagina qo'shilsin

class TarifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarif
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'

class KinoKinoAktyorPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = KinoAktyor
        fields = ('aktyor',)