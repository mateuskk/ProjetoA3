from django.shortcuts import render
from .models import Mesa, Reserva
from django.utils import timezone

def home(request):
    return render(request, 'reservation/home.html')

def atendente(request):
    mensagem = ""
    if request.method == "POST":
        if "criar" in request.POST:
            try:
                mesa_num = int(request.POST["mesa"])
                mesa = Mesa.objects.get(numero=mesa_num)
                data = request.POST["data"]
                hora = request.POST["hora"]
                quantidade = int(request.POST["quantidade_pessoas"])
                nome = request.POST["nome_responsavel"]
                # Verifica se já existe reserva para a mesa, data e hora
                existe = Reserva.objects.filter(mesa=mesa, data=data, hora=hora, status='reservada').exists()
                if existe:
                    mensagem = "Erro: Mesa já reservada para este horário."
                else:
                    reserva = Reserva.objects.create(
                        mesa=mesa,
                        data=data,
                        hora=hora,
                        quantidade_pessoas=quantidade,
                        nome_responsavel=nome,
                        status='reservada'
                    )
                    mensagem = f"Reserva criada com sucesso! ID da reserva: {reserva.id}"
            except Mesa.DoesNotExist:
                mensagem = "Mesa não encontrada."
            except Exception as e:
                mensagem = f"Erro ao criar reserva: {e}"
        elif "cancelar" in request.POST:
            try:
                reserva_id = int(request.POST["reserva_id"])
                reserva = Reserva.objects.get(id=reserva_id)
                reserva.status = 'cancelada'
                reserva.save()
                mensagem = "Reserva cancelada com sucesso!"
            except Reserva.DoesNotExist:
                mensagem = "Reserva não encontrada."
            except Exception as e:
                mensagem = f"Erro ao cancelar reserva: {e}"
    return render(request, 'reservation/attendant.html', {"mensagem": mensagem})

def garcom(request):
    mensagem = ""
    if request.method == "POST":
        try:
            reserva_id = int(request.POST["reserva_id"])
            garcom_nome = request.POST["garcom"]
            reserva = Reserva.objects.get(id=reserva_id)
            if reserva.status != 'reservada':
                mensagem = "Reserva não está disponível para confirmação."
            else:
                reserva.status = 'confirmada'
                reserva.garcom_confirmador = garcom_nome
                reserva.save()
                mensagem = "Reserva confirmada e mesa liberada para nova reserva futura."
        except Reserva.DoesNotExist:
            mensagem = "Reserva não encontrada."
        except Exception as e:
            mensagem = f"Erro ao confirmar reserva: {e}"
    return render(request, 'reservation/waiter.html', {"mensagem": mensagem})

def gerente(request):
    return render(request, 'reservation/manager.html')

def relatorios(request):
    tipo = request.GET.get("tipo")
    reservas = []
    mensagem = ""
    if tipo == "periodo":
        data_ini = request.GET.get("data_ini")
        data_fim = request.GET.get("data_fim")
        if data_ini and data_fim:
            reservas = Reserva.objects.filter(data__range=[data_ini, data_fim])
            if not reservas:
                mensagem = "Nenhuma reserva encontrada no período."
    elif tipo == "mesa":
        mesa_num = request.GET.get("mesa")
        if mesa_num:
            reservas = Reserva.objects.filter(mesa__numero=mesa_num)
            if not reservas:
                mensagem = "Nenhuma reserva encontrada para esta mesa."
    elif tipo == "garcom":
        garcom = request.GET.get("garcom")
        if garcom:
            reservas = Reserva.objects.filter(garcom_confirmador__iexact=garcom)
            if not reservas:
                mensagem = "Nenhuma reserva confirmada por este garçom."
    return render(request, 'reservation/reports.html', {"tipo": tipo, "reservas": reservas, "mensagem": mensagem})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('atendente/', views.atendente, name='atendente'),
    path('garcom/', views.garcom, name='garcom'),
    path('gerente/', views.gerente, name='gerente'),
    path('relatorios/', views.relatorios, name='relatorios'),
]