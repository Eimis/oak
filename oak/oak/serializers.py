from rest_framework import serializers
from oak import models as oak_models  # circular dependency


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = oak_models.Game
        fields = (
            'pk',
        )
