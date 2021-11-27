from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Fruit
from .serializers import FruitSerializer
from .permissions import IsOwnerOrReadOnly

class FruitsList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class FruitgDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    