from django.db import models
from django.contrib.auth.models import (
    User
)


class Profile(models.Model):
    name = models.CharField(max_length=60)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLES = (
        (1, 'Cliente'),
        (2, 'Lojista'),
    )

    role = models.PositiveIntegerField(choices=ROLES)

    def __str__(self):
        return f'{self.user.id} - {self.user.get_full_name()}'

    class Meta:
        verbose_name_plural = 'Perfís'
