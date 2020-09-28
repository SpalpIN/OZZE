from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Human)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.Shipment)
admin.site.register(models.OrderItems)
admin.site.register(models.CoatModel)
admin.site.register(models.DressModel)
admin.site.register(models.ParkaModel)
admin.site.register(models.FaceMaskModel)
admin.site.register(models.CartModel)