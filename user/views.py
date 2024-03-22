from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class TestingView(APIView):

    def get(self, request):
        hannan = "hannan"
        return Response(hannan)
