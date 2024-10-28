from django.db import models

# A Django model is a table in your database.
# Create your models here.


class Produto(models.Model):

    CATEGORIA_CHOICES = [
        ("PAD", "Padaria"),
        ("LEG", "Legume"),
        ("CAR", "Carne"),
        ("FRU", "Fruta"),
        ("BEB", "Bebida"),
    ]

    CATEGORIA_IMAGENS = [
        ("PAD", "img/icon/Type=bakery.svg"),
        ("LEG", "img/icon/Type=vegetable.svg"),
        ("CAR", "img/icon/Type=beef.png"),
        ("FRU", "img/icon/Type=fruit.svg"),
        ("BEB", "img/icon/Type=drink.svg"),
    ]

    TIPO = [("UN", "Un."), ("L", "L"), ("KG", "Kg")]

    id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    nome = models.CharField(max_length=42)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=3, choices=TIPO)
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES)
    concluida = models.BooleanField(default=False)
