from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from .models import Produto
from .forms import ProdutoModelForm


def home(request):
    produtos = Produto.objects.all()
    return render(request, 'app/index.html', {'produtos': produtos})


def produto_create(request):
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('app:home'))
    else:
        form = ProdutoModelForm()
    return render(request, 'app/inserir_produto.html', {'form': form})


def produto_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoModelForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect(reverse('app:home'))
    else:
        form = ProdutoModelForm(instance=produto)
    return render(request, 'app/atualizar_produto.html', {'form': form})


def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect(reverse('app:home'))
    return render(request, 'app/deletar_produto.html', {'produto': produto})