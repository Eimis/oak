from rest_framework.response import Response
from rest_framework.views import APIView

from oak.models import Game, GameLog
from oak.serializers import GameLogSerializer, GameSerializer


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
    serializer_class = GameLogSerializer

    http_method_names = ['post', ]

    def post(self, request, format=None):

        row = request.data.get('row', None)
        column = request.data.get('column', None)
        player = request.data.get('player', None)
        game = request.data.get('game', None)

        # we can't use all() here because 0's are False:
        if row is None or column is None or player is None or game is None:
            return Response({
                'error': ('Missing one of the required parameters: row, '
                          'column, player, and / or game')
            })

        log = GameLog.objects.create(
            to_row=row,
            to_column=column,
            player=player,
            game=Game.objects.get(pk=game),
        )
        serializer = GameLogSerializer(log)

        return Response(serializer.data)
