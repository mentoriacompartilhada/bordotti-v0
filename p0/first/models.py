from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=80)

    class Meta:
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.nome