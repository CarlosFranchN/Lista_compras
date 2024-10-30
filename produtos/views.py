# Django views are Python functions that take http requests and return http response, like HTML documents.
# Create your views here.
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
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


@csrf_exempt
def atualizarProduto(request):
    if request.method == "POST":
        produto_id = request.POST.get(
            "produto_id"
        )  # Certifique-se de que o campo id no formulário é 'produto_id'
        concluida = (
            request.POST.get("concluida") == "true"
        )  # Verifique se o valor está sendo passado como string 'true'

        try:
            produto = Produto.objects.get(id=produto_id)
            produto.concluida = concluida
            produto.save()
            return JsonResponse({"status": "success"})
        except Produto.DoesNotExist:
            return JsonResponse(
                {"status": "error", "message": "Produto não encontrado"}, status=404
            )
    else:
        return JsonResponse(
            {"status": "error", "message": "Método inválido"}, status=400
        )

def deletar_item(request, item_id):
    item = get_object_or_404(Produto, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect(produtos)  # Redirecionar para onde você quer
    return redirect(produtos)  # Se não for um POST, redirecionar para a lista