from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True, verbose_name = 'Avatar')

    class Meta:
        db_table = 'user'
        verbose_name= 'käyttäjä' 
        verbose_name_plural= 'käyttäjät'

    def __str__(self):
        return self.username

