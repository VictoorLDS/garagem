from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from garagem.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    fotos_attachment_key = SlugRelatedField(
        source="fotos",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    fotos = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoDetSerializer(ModelSerializer):
    fotos = ImageSerializer(required=False)
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1

class VeiculoListSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ["modelo", "ano", "preco"]