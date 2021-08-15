from django.db import models
from django.core.validators import RegexValidator

class Convidados(models.Model):
    nome = models.CharField(max_length=100, unique= True)
    idade = models.PositiveIntegerField()
    NOIVO = 'Noivo'
    NOIVA = 'Noiva'
    TIPO = [
        (NOIVO,'Noivo'),
        (NOIVA,'Naiva'),
    ]
    tipo = models.CharField(max_length=5, choices=TIPO)
    email = models.EmailField(max_length=100, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telefone = models.CharField(validators=[phone_regex], max_length=15)

    def __str__(self):
        return self.nome
