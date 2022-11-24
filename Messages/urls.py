from django.urls import path
from . import views

app_name='messages'

urlpatterns = [
    path('messages/send',views.send_message_view,name= 'send_message'),
]