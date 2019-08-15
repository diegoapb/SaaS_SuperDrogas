# admin.models.py

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Role(TimeStampedModel):

    USER_TYPE_CHOICES = (
        (1, 'administrador'),
        (2, 'cliente_online'),
        (3, 'vendedor_tpv'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, primary_key=True)


@receiver(post_save, sender=User)
def create_user_role(sender, instance, created, **kwargs):
    if created:
            Rolees.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_role(sender, instance, **kwargs):
    instance.role.save()
