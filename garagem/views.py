from rest_framework.viewsets import ModelViewSet

from garagem.models import Marca
from garagem.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.object.all()
    serializers_class = MarcaSerializer