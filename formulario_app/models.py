from django.db import models

class Formulario(models.Model):
    PLANETAS_ORIGEM_CHOICES = [
        ('Terra', 'Planeta Terra'),
        ('Namek', 'Planeta Namek'),
        ('Vegeta', 'Planeta Vegeta'),
        ('Outros', 'Outros')
    ]

    RACA_PREFERIDA_CHOICES = [
        ('Terráqueo', 'Terráqueo'),
        ('Sayajin', 'Sayajin'),
        ('Androide', 'Androide'),
        ('Outros', 'Outros')
    ]

    TRABALHO_CHOICES = [
        ('Autonomo', 'Autonomo'),
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('Tipo Goku', 'Tipo Goku')
    ]

    ACAI_CHOICES = [
        ('Puro', 'Puro'),
        ('Com banana', 'Com banana'),
        ('Com granola', 'Com granola'),
        ('Com gosto de terra', 'Com gosto de terra')
    ]

    TAMANHO_CHOICES = [
        ('300ml', '300ml'),
        ('500ml', '500ml'),
        ('1000ml', '1000ml'),
        ('Casquinha', 'Casquinha')
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    planeta_origem = models.CharField(max_length=20, choices=PLANETAS_ORIGEM_CHOICES)
    raca_preferida = models.CharField(max_length=20, choices=RACA_PREFERIDA_CHOICES)
    trabalho = models.CharField(max_length=20, choices=TRABALHO_CHOICES)
    acai_preferido = models.CharField(max_length=20, choices=ACAI_CHOICES)
    tamanho_preferido = models.CharField(max_length=20, choices=TAMANHO_CHOICES)
    observacoes = models.TextField()