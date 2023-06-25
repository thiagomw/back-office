from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente, Maquina
from .templates.clientes.forms import CustomRegistroForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def adicionar_cliente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        unidade = request.POST['unidade']
        endereco = request.POST['endereco']
        email = request.POST['email']
        telefone = request.POST['telefone']
        cliente = Cliente(nome=nome, unidade=unidade,
                          endereco=endereco, email=email, telefone=telefone)
        cliente.save()
        return redirect('listar_clientes')
    return render(request, 'adicionar_cliente.html')


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})


def visualizar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render(request, 'clientes/visualizar_cliente.html', {'cliente': cliente})


def buscar_clientes(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        clientes = Cliente.objects.filter(nome__icontains=nome)
        return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})
    return render(request, 'clientes/buscar_clientes.html')


def registrar(request):
    if request.method == 'POST':
        form = CustomRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegistroForm()
    return render(request, 'registrar.html', {'form': form})


# Visualizações para máquinas alugadas


def adicionar_maquina(request):
    if request.method == 'POST':
        cliente_id = request.POST['cliente']
        cliente = Cliente.objects.get(pk=cliente_id)
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        processador = request.POST['processador']
        memoria = request.POST['memoria']
        ssd = request.POST['ssd']
        observacao = request.POST['observacao']
        maquina = Maquina(
            cliente=cliente, marca=marca, modelo=modelo, processador=processador, memoria=memoria, ssd=ssd, observacao=observacao)
        maquina.save()
        return redirect('listar_maquinas')
    clientes = Cliente.objects.all()
    return render(request, 'adicionar_maquina.html', {'clientes': clientes})


def listar_maquinas(request):
    maquinas = Maquina.objects.all()
    return render(request, 'listar_maquinas.html', {'maquinas': maquinas})
