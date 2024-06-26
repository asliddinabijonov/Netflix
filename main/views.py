from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import *
from .serializers import *


class IndexAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "xabar": "Salom dunyo",
                "framework": "django rest framework"
            }
        )

    def post(self, request):
        pass

    def delete(self):
        pass


class AktyorlarAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            Aktyor.objects.create(
                ism=data.get('ism'),
                davlat=data.get('davlat'),
                jins=data.get('jins'),
                t_yil=data.get('t_yil'),
            )
            return Response("Aktyor yaratildi", status=201)
        return Response(serializer.errors, status=400)


class AktyorTahrirlashAPIView(APIView):
    def put(self, request, pk):
        serializer = AktyorSerializer(data=request.data)
        if serializer.is_valid():
            aktyorlar = Aktyor.objects.filter(id=pk).update(
                ism=serializer.data.get('ism'),
                davlat=serializer.data.get('davlat'),
                jins=serializer.data.get('jins'),
                t_yil=serializer.data.get('t_yil'),
            )
            return Response(
                {
                    "success": True,
                    "updated_data": serializer.data
                }
            )
        return Response(serializer.errors, status=400)


# class KinolarAPIView(APIView):
#     def get(self, request):
#         nom_search = request.query_params.get('nom', None)
#         yil_search = request.query_params.get('yil', None)
#         yil_order = request.query_params.get('yil_order', None)
#         kinolar = Kino.objects.all()
#         if nom_search is not None:
#             kinolar = kinolar.filter(nom__icontains=nom_search)
#         if yil_search is not None:
#             kinolar = kinolar.filter(yil=yil_search)
#
#         if yil_order is not None:
#             if yil_order == 'new':
#                 kinolar = kinolar.order_by('-yil')
#             elif yil_order == 'old':
#                 kinolar = kinolar.order_by('yil')
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = KinoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


#
#
# class KinoTahrirlashAPIView(APIView):
#     def put(self, request, pk):
#         kino = get_object_or_404(Kino, pk=pk)
#         serializer = KinoSerializer(kino, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


class IzohlarModelViewSet(ModelViewSet):
    queryset = Izoh.objects.all()
    serializer_class = IzohSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['kino__nom', 'matn', 'baho']
    ordering_fields = ['sana', 'baho']

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get_queryset(self):
        izohlar = Izoh.objects.filter(user=self.request.user,baho__gte=2)
        return izohlar

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return status.HTTP_201_CREATED

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("Izoh ochirilmadi")
        instance.delete()


class KinolarModelViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nom', 'janr']
    ordering_fields = ['janr', 'yil']

    @action(detail=True, methods=['get'])
    def aktyorlar(self, request, pk):
        kino = self.get_object()
        kino_akytorlar = KinoAktyor.objects.filter(kino=kino).values_list('aktyor__id', flat=True)
        aktyorlar = Aktyor.objects.filter(id__in=kino_akytorlar)
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=['post'], serializer_class=KinoKinoAktyorPostSerializer)
    def aktyor_add(self, request, pk):
        kino = self.get_object()
        serializer = KinoKinoAktyorPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


# class TariflarAPIView(APIView):
#     def get(self, request):
#         min_narx = request.query_params.get('min', None)
#         max_narx = request.query_params.get('max', None)
#         tariflar = Tarif.objects.all()
#         if min_narx is not None:
#             tariflar = tariflar.filter(narx__gte=min_narx)
#
#         if max_narx is not None:
#             tariflar = tariflar.filter(narx__lte=max_narx)
#         serializer = TarifSerializer(tariflar, many=True)
#         return Response(serializer.data, status=200)

class TariflarModelViewSet(ModelViewSet):
    queryset = Tarif.objects.all()
    serializer_class = TarifSerializer

    def get_queryset(self):
        min_narx = self.request.query_params.get('min', None)
        max_narx = self.request.query_params.get('max', None)
        tariflar = Tarif.objects.all()
        if min_narx is not None:
            tariflar = tariflar.filter(narx__gte=min_narx)

        if max_narx is not None:
            tariflar = tariflar.filter(narx__lte=max_narx)

        return tariflar