from django.test import TestCase
from .models import Produto

class ProdutoModelTest(TestCase):

    def setUp(self):
        # Criando instâncias de Produto para o teste
        Produto.objects.create(nome="Maçã", quantidade=5, tipo="KG", categoria="FRU")
        Produto.objects.create(nome="Pão", quantidade=10, tipo="UN", categoria="PAD")

    def test_produto_queryset(self):
        # Testa se o método Produto.objects.all() retorna os produtos criados no setUp
        produtos = Produto.objects.all()
        print("Carlos")
        print(produtos[0].nome)
        self.assertEqual(produtos.count(), 2)  # Verifica se temos dois produtos
        self.assertEqual(produtos[0].nome, "Maçã")
        self.assertEqual(produtos[1].nome, "Pão")
