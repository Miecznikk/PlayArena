from django.contrib import admin

from .models import Match, Stadium, Goal

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['team1','team2','stadium','date','status','referee']

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['name','location']

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['scorer','match','team']

# Register your models here.
