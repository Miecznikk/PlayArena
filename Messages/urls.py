from django.urls import path
from . import views

app_name='messages'

urlpatterns = [
    path('messages/send',views.send_message_view,name= 'send_message'),
    path('messages/my_messages',views.my_messages_view,name='my_messages'),
    path('messages/send/?P<int:receiver>',views.send_message_view,name='send_message_to'),
    path('messages/delete/?<int:message>',views.delete_message,name='delete_message'),
    path('messages/send_invite',views.send_invite_view,name='send_invite'),
    path('messages/accept_invite/?<int:message>',views.accept_invite,name='accept_invite'),
    path('messages/send_challenge',views.send_challenge,name='send_challenge'),
]