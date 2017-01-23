from django.contrib import admin
from .models import Product
from . import models

admin.site.register(Product)
admin.site.register(models.User)
admin.site.register(models.Batch)
admin.site.register(models.Course)
admin.site.register(models.Bill)

