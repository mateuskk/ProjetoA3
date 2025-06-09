from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)
    capacidade = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero} ({self.capacidade} pessoas)"

class Reserva(models.Model):
    STATUS_CHOICES = [
        ('reservada', 'Reservada'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    quantidade_pessoas = models.IntegerField()
    nome_responsavel = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='reservada')
    garcom_confirmador = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nome_responsavel} - Mesa {self.mesa.numero} em {self.data} às {self.hora}"