# Generated by Django 5.0.2 on 2024-08-12 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_remove_livro_autor_remove_livro_coautor_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="autores",
            new_name="autor",
        ),
    ]
