from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    image = models.ImageField(default='user.png', 
    upload_to="profile/%Y/%m/%d", blank=True, null=True, verbose_name="Imagem(opcional)")
    bio = models.TextField(default="Escreva sobre você...", max_length=300, 
    verbose_name="Conte-nos sobre você", blank=True, null=True)

    
    def __str__(self):
        return f'{self.user.username} Perfil'

    class Meta:
        verbose_name = 'Perfil'    
        verbose_name_plural = 'Perfis'


        