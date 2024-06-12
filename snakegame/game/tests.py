# game/tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import GameScore
from .serializers import GameScoreSerializer


class GameScoreTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('gamescore-list')

    def test_create_game_score(self):
        data = {'player_name': 'TestPlayer', 'score': 100}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameScore.objects.count(), 1)
        self.assertEqual(GameScore.objects.get().player_name, 'TestPlayer')

    def test_get_game_scores(self):
        GameScore.objects.create(player_name='Player1', score=100)
        GameScore.objects.create(player_name='Player2', score=200)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['player_name'], 'Player2')
        self.assertEqual(response.data[0]['score'], 200)
        self.assertEqual(response.data[1]['player_name'], 'Player1')
        self.assertEqual(response.data[1]['score'], 100)
