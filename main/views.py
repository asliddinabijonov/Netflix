from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(
            aktyorlar, many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            Aktyor.objects.create(
                ism=data.get('ism'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
                t_yil=data.get('t_yil')
            )
            return Response('Aktyor yaratildi', status=201)
        return Response(serializer.errors, status=400)


class AktyorTahrirlashAPIView(APIView):
    def put(self, request, pk):
        aktyor = get_object_or_404(Aktyor, id=pk)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            data = serializer.data
            aktyor = Aktyor.objects.filter(id=pk).update(
                ism=data.get('ism'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
                t_yil=data.get('t_yil')
            )
            return Response(
                {
                    "success": True,
                    "updated_data": serializer.data
                }, status=200
            )
        return Response(serializer.errors, status=400)


class AktyorDetailsAPIView(APIView):
    def get(self, request, pk):
        aktyor = get_object_or_404(Aktyor, id=pk)
        serializer = AktyorSerializer(aktyor)
        return Response(serializer.data)


class AktyorDeleteAPIView(APIView):
    def delete(self, request, pk):
        aktyor = get_object_or_404(Aktyor, id=pk)
        aktyor.delete()
        return Response("Aktyor ochirildi", status=204)

class TariflarAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(
            tariflar, many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TarifSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            Tarif.objects.create(
                nom=data.get('nom'),
                narx=data.get('narx'),
                davomiylik=data.get('davomiylik'),
            )
            return Response('Tarif yaratildi', status=201)
        return Response(serializer.errors, status=400)

class TarifTahrirlashAPIView(APIView):
    def put(self, request, pk):
        tarif = get_object_or_404(Tarif, id=pk)
        serializer = TarifSerializer(tarif, data=request.data)
        if serializer.is_valid():
            data = serializer.data
            tarif = Tarif.objects.filter(id=pk).update(
                nom=data.get('nom'),
                narx=data.get('narx'),
                davomiylik=data.get('davomiylik'),
            )
            return Response(
                {
                    "success": True,
                    "updated_data": serializer.data
                }, status=200
            )
        return Response(serializer.errors, status=400)

class TarifDetailsAPIView(APIView):
    def get(self, request, pk):
        tarif = get_object_or_404(Aktyor, id=pk)
        serializer = TarifSerializer(tarif)
        return Response(serializer.data)


class TarifDeleteAPIView(APIView):
    def delete(self, request, pk):
        tarif = get_object_or_404(Aktyor, id=pk)
        tarif.delete()
        return Response("Aktyor ochirildi", status=204)