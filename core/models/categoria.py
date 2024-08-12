from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

    # class Meta:
    #     verbose_name = "Prateleira"
    #     verbose_name_plural = "Prateleiras"
