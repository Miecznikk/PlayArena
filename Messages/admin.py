from django.contrib import admin
from .models import Message
@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    list_display = ['sender','receiver','title','description']
    readonly_fields = ('created',)

# Register your models here.
