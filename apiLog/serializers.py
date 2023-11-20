from rest_framework import serializers

from shopApp.models import LoggingMoves


class LoggingMovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggingMoves
        fields = '__all__'

