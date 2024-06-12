# game/serializers.py

from rest_framework import serializers
from .models import GameScore

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        fields = ['id', 'player_name', 'score']  # Add 'player_name' field here
