from django.db import models

from .categoria import Categoria
from .editora import Editora
from .autor import Autor


class Livro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name="Preço")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros", blank=True, null=True)

    def __str__(self):
        return f"({self.id}) {self.titulo} ({self.quantidade})"
