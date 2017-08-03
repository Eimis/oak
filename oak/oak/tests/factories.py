import factory.django

from oak.models import Game


class GameFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Game
