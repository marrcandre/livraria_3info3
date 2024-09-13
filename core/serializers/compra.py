from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("quantidade", "livro")
        depth = 1

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(read_only=True, many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "itens")
