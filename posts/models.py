from django.db import models
from django.utils import timezone


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=150)
    conteudo = models.TextField()
    imagem = models.ImageField(null=False, blank=False, upload_to='images/')
    publicado = models.DateTimeField(default=timezone.now)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
