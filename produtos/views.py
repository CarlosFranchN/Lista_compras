# Django views are Python functions that take http requests and return http response, like HTML documents.
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .form import ProdutoForm
from .models import Produto
from django.views.decorators.csrf import csrf_exempt


# def produtos(request):
#     template = loader.get_template("./main.html")
#     return HttpResponse(template.render())


def BuscarProdutos():
    produtos = Produto.objects.all()
    return produtos


def BuscarOptions():
    categorias = Produto.CATEGORIA_CHOICES
    tipos = Produto.TIPO
    options = {"categorias": categorias, "tipos": tipos}
    return options


def BuscarIcones():
    icones = Produto.CATEGORIA_IMAGENS
    print(icones)
    return icones


@csrf_exempt
def produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)

        # Exibir dados recebidos no terminal
        print("Dados recebidos do formulário:", request.POST)

        if form.is_valid():
            # Exibir dados validados
            print("Dados validados:", form.cleaned_data)

            # Salvar os dados no banco de dados
            form.save()

            # Exibir uma confirmação no terminal
            print("Produto salvo com sucesso no banco de dados!")

            # Redirecionar após o sucesso do submit
            return redirect("produtos")
        else:
            # Se houver erros de validação, exibi-los no terminal
            print("Erros no formulário:", form.errors)
    else:
        # Se o método não for POST, exibir o formulário vazio
        form = ProdutoForm()
    produtos = BuscarProdutos()  # Busca todos os produtos no banco de dados
    options = BuscarOptions()
    icones = BuscarIcones()
    print(icones)
    # Renderizar o template e passar o formulário
    return render(
        request,
        "main.html",
        {"form": form, "produtos": produtos, "options": options, "icones": icones},
    )


def card(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco de dados
    return render(request, "card.html", {"produtos": produtos})
