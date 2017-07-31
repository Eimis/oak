from rest_framework.response import Response
from rest_framework.views import APIView

from oak.models import Game
from oak.serializers import GameSerializer


class GameInitializationView(APIView):
    '''An API view to create a new Game object when a new game is initialised
    via frontend
    '''
    permission_classes = (
    )
    serializer_class = GameSerializer

    http_method_names = ['get', ]

    def get(self, request, format=None):

        game = Game.objects.last()
        serializer = GameSerializer(game)

        return Response(serializer.data)


class GameActionView(APIView):
    '''An API view to log game action
    '''
    permission_classes = (
    )

    http_method_names = ['get', ]

    def get(self, request, format=None):

        resp = {'a': 'b'}

        return Response(resp)
