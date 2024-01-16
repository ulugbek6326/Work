from django.shortcuts import render

from rest_framework import generics

from .serializers import WorkerSerializer, OrdererSerializer

from .models import Worker, Orderer
# Create your views here.
# worker list and create

class WorkerListView(generics.ListAPIView):
    serializer_class = WorkerSerializer
    
    def get_queryset(self):
        queryset = Worker.objects.all()
        search_param = self.request.query_params.get('search', None)

        if search_param:
            queryset = queryset.filter(job__icontains=search_param)
                       
        return queryset
    
class WorkerCreateView(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    
# Orderer list and create
    
class OrdererListView(generics.ListAPIView):
    queryset = Orderer.objects.all()
    serializer_class = OrdererSerializer
    
class OrdererCreateView(generics.CreateAPIView):
    queryset = Orderer.objects.all()
    serializer_class = OrdererSerializer