"""Administrador models"""

from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)


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


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()


class OrderItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    # country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)

    # same_shipping_address = models.CharField(max_length=100)
    # save_info = models.CharField(max_length=100)
    # payment_option = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
