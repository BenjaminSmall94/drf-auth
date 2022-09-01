from .models import House
from .serializers import HouseSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class HouseList(ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseDetail(RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseUpdate(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class HouseCreate(ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
