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

    # FIXME: use rows and columns?:
    from_column = models.CharField(max_length=1, choices=GAME_COLUMN_CHOICES)
    to_column = models.CharField(max_length=1, choices=GAME_COLUMN_CHOICES)
    player = models.CharField(max_length=1, choices=GAME_PLAYER_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game)
