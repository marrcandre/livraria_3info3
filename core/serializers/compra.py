from rest_framework.serializers import (
    CharField,
    CurrentUserDefault,
    HiddenField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from core.models import Compra, ItensCompra


class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ("quantidade", "total", "livro")
        depth = 1


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")

    def validate_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValidationError("A quantidade deve ser maior que zero.")
        return quantidade

    def validate(self, item):
        if item["quantidade"] > item["livro"].quantidade:
            raise ValidationError("Quantidade de itens maior do que a quantidade em estoque.")
        return item


class ListarItensCompraSerializer(ModelSerializer):
    livro = CharField(source="livro.titulo", read_only=True)

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
        fields = ("id", "usuario", "status", "total", "itens")


class CriarEditarCompraSerializer(ModelSerializer):
    usuario = HiddenField(default=CurrentUserDefault())
    itens = CriarEditarItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra

    def update(self, compra, validated_data):
        itens_data = validated_data.pop("itens")
        if itens_data:
            compra.itens.all().delete()
            for item_data in itens_data:
                ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return super().update(compra, validated_data)


class ListarCompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    itens = ListarItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")
