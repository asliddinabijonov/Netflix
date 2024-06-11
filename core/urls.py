from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('aktyorlar/<int:pk>/', AktyorDetailsAPIView.as_view()),
    path('aktyorlar/<int:pk>/delete/', AktyorDeleteAPIView.as_view()),
    path('aktyorlar/<int:pk>/tahrirlash/', AktyorTahrirlashAPIView.as_view()),
    path('tariflar/', TariflarAPIView.as_view()),
    path('tariflar/<int:pk>/tahrirlash/', TarifTahrirlashAPIView.as_view()),
    path('tariflar/<int:pk>/', TarifDetailsAPIView.as_view()),
    path('tariflar/<int:pk>/delete/', TarifDeleteAPIView.as_view()),
]
