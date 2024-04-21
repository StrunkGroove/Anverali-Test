from django.contrib.auth.models import User
from django.db import models

from freelancer.models import Direction
 

class Customer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, 
        related_name='customer'
    )
    description = models.TextField(verbose_name='Описание профиля')
    contact_method = models.CharField(
        max_length=100,
        verbose_name='Метод связи'
    )

    def __str__(self):
        return f'{self.user.username}'
    

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма заказа'
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    directions = models.ManyToManyField(
        Direction,
        blank=True,
        verbose_name='Направления'  
    )

    def __str__(self):
        return f'{self.name}, {self.amount}, {self.customer}'
    