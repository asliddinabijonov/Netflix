from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from main.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('izohlar', IzohlarModelViewSet)

router.register('kinolar', KinolarModelViewSet)
router.register('tariflar', TariflarModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexAPIView.as_view()),
    path('token/', obtain_auth_token),
    path('aktyorlar/', AktyorlarAPIView.as_view()),
    path('aktyorlar/<int:pk>/tahrirlash/', AktyorTahrirlashAPIView.as_view()),
    # path('tariflar/', TariflarAPIView.as_view()),

    # path('kinolar/', KinolarAPIView.as_view()),
    # path('kinolar/<int:pk>/tahrirlash/', KinoTahrirlashAPIView.as_view()),

    path('', include(router.urls)),
]
