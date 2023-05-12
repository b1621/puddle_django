from django.contrib import admin

from .models import Category, Item
# .models cause it is in the same folder

admin.site.register(Category)
admin.site.register(Item)