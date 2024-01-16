from django.urls import path

from .views import WorkerCreateView, WorkerListView, OrdererListView, OrdererCreateView

urlpatterns = [
    path('work_list/', WorkerListView.as_view()),
    path('work_create/', WorkerCreateView.as_view()),
    
    path('orderer_list/', OrdererListView.as_view()),
    path('orderer_create/', OrdererCreateView.as_view()),
]
