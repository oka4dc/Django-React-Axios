from django.conf import settings
from App.models import React
from rest_framework import serializers

class Reactserializers(serializers.ModelSerializer):
    class Meta:
        model: React
        fields: "__all__"
