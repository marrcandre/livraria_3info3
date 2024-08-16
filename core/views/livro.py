from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroDetailSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.order_by("titulo")
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
