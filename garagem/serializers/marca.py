from garagem.models.marca import Marca
from rest_framework.serializers import ModelSerializer


class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"