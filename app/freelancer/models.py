from django.contrib.auth.models import User
from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Freelancer(models.Model):
    EXPERIENCE_CHOICES = [
        (1, 'Менее 1 года'),
        (2, '1-3 года'),
        (3, '3-5 лет'),
        (4, 'Более 5 лет')
    ]

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='freelancer'
    )
    experience = models.IntegerField(
        choices=EXPERIENCE_CHOICES,
        null=True,
        blank=True,
        verbose_name='Опыт'
    )
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    directions = models.ManyToManyField(
        Direction,
        blank=True,
        verbose_name='Направления'  
    )
    contact_info = models.CharField(
        max_length=100,
        verbose_name='Метод связи'
    )