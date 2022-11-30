from django.contrib import admin
from .models import Message,Invite,Challenge

@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['sender','receiver','title','description']
    readonly_fields = ('created',)

@admin.register(Invite)
class AdminInvite(admin.ModelAdmin):
    list_display = ['sender','receiver','title','description','invited_to']
    readonly_fields = ('created',)

@admin.register(Challenge)
class AdminChallenge(admin.ModelAdmin):
    list_display = ['sender','receiver','title','description','challenged_team',
                    'challenging_team','stadium','date']
# Register your models here.
