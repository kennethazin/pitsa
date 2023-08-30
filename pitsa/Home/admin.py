from django.contrib import admin
from .models import PizzaSize, PizzaCrust, PizzaSauce, PizzaTopping, Cheese

admin.site.register(PizzaSize)
admin.site.register(PizzaCrust)
admin.site.register(PizzaSauce)
admin.site.register(PizzaTopping)
admin.site.register(Cheese)

