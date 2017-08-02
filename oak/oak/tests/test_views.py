import json

from django.core.urlresolvers import reverse
from django.test import TestCase


class GameApiViewTests(TestCase):

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
