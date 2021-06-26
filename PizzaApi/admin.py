from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PizzaSize)
admin.site.register(PizzaType)
admin.site.register(PizzaTopping)
admin.site.register(Pizza)
