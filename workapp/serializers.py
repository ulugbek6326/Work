from rest_framework import serializers
from . models import Worker, Orderer


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
        
        
class OrdererSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderer
        fields = '__all__'