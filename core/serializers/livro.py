from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "preco")

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

