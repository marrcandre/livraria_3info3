# Generated by Django 5.1 on 2024-08-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_livro_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="editora",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
