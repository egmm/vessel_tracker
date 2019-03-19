from rest_framework import serializers


class ShipsSerializer(serializers.Serializer):
    imo = serializers.CharField()
    name = serializers.CharField()


class PositionSerializer(serializers.Serializer):
    ship = ShipsSerializer(source='imo')
    timestamp = serializers.DateTimeField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
