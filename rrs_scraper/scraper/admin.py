from django.contrib import admin

from .models import Feed, Item

# Register your models here.
admin.site.register(Feed)
admin.site.register(Item)
