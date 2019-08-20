"""Administrador models"""

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(TimeStampedModel):

    USER_TYPE_CHOICES = (
        (1, 'Administrador'),
        (2, 'Vendedor'),
        (3, 'Cliente Online'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, primary_key=True, default=3)

    def __str__(self):
        """Return Username"""
        return self.user.username


@receiver(post_save, sender=User)
def create_user_role(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Role.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_role(sender, instance, **kwargs):
    instance.role.save()
