from rest_framework import serializers
from .models import ModelA, ModelB, ModelC

class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelA
        fields = '__all__'

class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = '__all__'

class ModelCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelC
        fields = '__all__'
