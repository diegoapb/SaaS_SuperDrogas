from django.contrib import admin

from .models import Role
from .models import Item, OrderItem, Order


# Admin models
admin.site.register(Role)

# Products

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)