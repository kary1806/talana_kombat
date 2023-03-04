from rest_framework import serializers


class Kombat(serializers.Serializer):
    player1 = serializers.JSONField(required=True)
    player2 = serializers.JSONField(required=True)
