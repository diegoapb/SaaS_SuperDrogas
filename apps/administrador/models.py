"""Administrador models"""

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Role(TimeStampedModel):
    USER_TYPE_CHOICES = (
        (1, 'Administrador'),
        (2, 'Vendedor'),
        (3, 'Cliente online'),
    )
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, default=3)

    def __str__(self):
        """Return Username"""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_role(sender, instance, created, **kwargs):
    if created:
        Role.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_role(sender, instance, **kwargs):
    instance.role.save()
