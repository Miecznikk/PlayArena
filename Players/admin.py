from django.contrib import admin
from .models import Player, Position

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name','second_name','surname','position','team']

# Register your models here.
