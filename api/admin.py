from django.contrib import admin

from .models import Item,Inventory,Sale

admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Sale)