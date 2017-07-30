from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class SetActionView(APIView):
    permission_classes = (
    )

    http_method_names = ['get', ]

    def get(self, request, format=None):

        resp = {'a': 'b'}

        return Response(resp)
