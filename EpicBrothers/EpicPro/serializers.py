from .models import Juegos
from rest_framework import serializers

class JuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juegos
        fields = '__all__'