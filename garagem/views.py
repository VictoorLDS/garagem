from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio, Categoria, Cor, Marca, Veiculo
from garagem.serializers import AcessorioSerializer, CategoriaSerializer,CorSerializer, MarcaSerializer, VeiculoSerializer, VeiculoDetSerializer, VeiculoListSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = {"list": VeiculoListSerializer, "retrieve": VeiculoDetSerializer}
    def get_serializer_class(self):
        return self.serializer_class.get(self.action, VeiculoSerializer)