from django.contrib import admin
from .models import Player,Position,Referee

@admin.register(Player)
class AdminPlayer(admin.ModelAdmin):
    list_display = ['first_name','second_name','surname','position','team','captain','image']

@admin.register(Position)
class AdminPosition(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Referee)
class AdminReferee(admin.ModelAdmin):
    list_display = ['first_name','second_name','surname','image']

# Register your models here.
