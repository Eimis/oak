import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from oak.models import Game, GameLog
from oak.serializers import DATE_FORMAT
from oak.tests.factories import GameFactory


class GameApiViewTests(TestCase):

    def setUp(self):
        self.test_game = GameFactory()

    def test_game_log_view_invalid_parameters(self):
        '''A test to test if GameLogView API endpoint returns correct data
        if POST parameters are missing
        '''
        url = reverse('log_game')

        response = self.client.post(
            url,
            {
                'row': '0',
                'column': '0',
                'player': 'X',
                # 'game': '1',
            },
        )

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)

        self.assertEqual(
            response_data['error'],
            'Missing one of the required parameters: row, column, player, and / or game'
        )

    def test_game_log_view(self):
        '''A test to test if GameLogView API endpoint returns correct data
        and new GameLog object is created
        '''
        url = reverse('log_game')

        post_data = {
            'row': '0',
            'column': '0',
            'player': 'X',
            'game': self.test_game.pk,
        }

        game_logs_before = GameLog.objects.count()

        response = self.client.post(
            url,
            post_data,
        )

        self.assertEqual(response.status_code, 200)
        game_logs_after = GameLog.objects.count()

        self.assertEqual(game_logs_after, game_logs_before + 1)

        response_data = json.loads(response.content)

        self.assertEqual(
            response_data,
            {
                'added_on_date': self.test_game.added_on.strftime(DATE_FORMAT),
                'game': self.test_game.pk,
                'id': self.test_game.pk,
                'player': post_data['player'],
                'to_column': post_data['column'],
                'to_row': post_data['row']
            }
        )
