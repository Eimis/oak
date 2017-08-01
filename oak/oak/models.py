from django.db import models


class Game(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)


class GameLog(models.Model):
    GAME_PLAYER_CHOICES = (
        ('X', 'X'),
        ('O', 'O'),
    )
    GAME_FIELD_CHOICES = (
        ('X', 'X'),
        ('O', 'O'),
    )

    # FIXME: use rows and columns?:
    from_column = models.CharField(max_length=1, choices=GAME_FIELD_CHOICES)
    to_column = models.CharField(max_length=1, choices=GAME_FIELD_CHOICES)
    player = models.CharField(max_length=1, choices=GAME_PLAYER_CHOICES)
    added_on = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game)
