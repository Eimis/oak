from rest_framework import serializers
from oak import models as oak_models  # circular dependency


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = oak_models.Game
        fields = (
            'pk',
        )


class GameLogSerializer(serializers.ModelSerializer):
    # This field is explicitly defined because we want to use different
    # date format and defining this setting globally probably isn't a very good
    # idea. Also, it'seasier to test this field.
    added_on_date = serializers.DateTimeField(
        source='added_on', format=DATE_FORMAT
    )

    class Meta:
        model = oak_models.GameLog
        fields = (
            'game',
            'id',
            'player',
            'to_column',
            'to_row',
            'added_on_date',
        )
