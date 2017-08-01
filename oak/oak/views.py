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

        # game = Game.objects.last()
        game = Game.objects.create()
        serializer = GameSerializer(game)

        return Response(serializer.data)


class GameLogView(APIView):
    '''An API view to log game action
    '''
    permission_classes = (
    )

    http_method_names = ['post', ]

    def post(self, request, format=None):

        row = request.data.get('row', None)
        column = request.data.get('column', None)
        player = request.data.get('player', None)
        game = request.data.get('game', None)

        if not all([row, column, player, game]):
            return Response({
                'error': ('Missing one of the required parameters: row, '
                          'column, player, and / or game')
            })

        # TODO:
        # only log if CORRECT player clicks

        return Response({})
