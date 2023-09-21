from rest_framework import serializers

class agencyDetailsSerializer(serializers.Serializer):
    agencyName = serializers.CharField()
    agencyID = serializers.CharField()
    type = serializers.CharField()
    frequency = serializers.FloatField()
    emergency = serializers.CharField()
    SOPs = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()