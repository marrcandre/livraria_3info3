from rest_framework.serializers import ModelSerializer

from core.models import Livro


class LivroDetailSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"

