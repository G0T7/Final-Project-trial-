# views.py

from django.shortcuts import render
from rest_framework import viewsets
from .models import GameScore
from .serializers import GameScoreSerializer

class GameScoreViewSet(viewsets.ModelViewSet):
    queryset = GameScore.objects.all().order_by('-score')
    serializer_class = GameScoreSerializer

# Global variables for game state
snake = [(0, 0)]
direction = (1, 0)
game_over = False

# Constants
GRID_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20

def move_snake():
    global snake, direction, game_over

    if not game_over:
        # Calculate the new head position
        head = snake[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])

        # Check for collisions
        if new_head in snake or new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
            game_over = True
            return

        # Move snake
        snake = [new_head] + snake[:-1]

def change_direction(new_direction):
    global direction

    # Prevent the snake from reversing
    if (direction[0] == 0 and new_direction[0] != 0) or (direction[1] == 0 and new_direction[1] != 0):
        direction = new_direction

def reset_game():
    global snake, direction, game_over
    snake = [(0, 0)]
    direction = (1, 0)
    game_over = False
