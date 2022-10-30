from django.contrib import admin

from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
