from rest_framework.viewsets import ModelViewSet

from garagem.models import Veiculo
from garagem.serializers import VeiculoSerializer, VeiculoDetSerializer, VeiculoListSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = {"list": VeiculoListSerializer, "retrieve": VeiculoDetSerializer}
    def get_serializer_class(self):
        return self.serializer_class.get(self.action, VeiculoSerializer)