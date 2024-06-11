from rest_framework import serializers


class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ism = serializers.CharField(max_length=255)
    davlat = serializers.CharField(max_length=50)
    jins = serializers.CharField(max_length=10)
    t_yil = serializers.DateField(required=False)

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nom = serializers.CharField(max_length=255)
    narx = serializers.FloatField()
    davomiylik = serializers.CharField(max_length=50)

