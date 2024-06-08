from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *

class IndexAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "xabar": "Salom dunyo",
                "framework": "django rest framework"
            }
        )

    def post(self,request):
        pass

    def delete(self):
        pass