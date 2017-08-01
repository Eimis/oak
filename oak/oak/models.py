from django.db import models


class Game(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)


class GameLog(models.Model):
    GAME_PLAYER_CHOICES = (
        ('X', 'X'),
        ('O', 'O'),
    )
    GAME_COLUMN_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    )
    GAME_ROW_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
    )

    added_on = models.DateTimeField(auto_now_add=True)

    to_column = models.CharField(max_length=1, choices=GAME_COLUMN_CHOICES)
    to_row = models.CharField(max_length=1, choices=GAME_ROW_CHOICES)

    player = models.CharField(max_length=1, choices=GAME_PLAYER_CHOICES)
    game = models.ForeignKey(Game)
