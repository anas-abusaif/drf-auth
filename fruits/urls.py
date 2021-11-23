
from django.urls import path
from .views import FruitsList, FruitgDetail

urlpatterns = [
    path('', FruitsList.as_view(), name='fruits-list'),
    path('<int:pk>/', FruitgDetail.as_view(), name='fruit-detail'),
]