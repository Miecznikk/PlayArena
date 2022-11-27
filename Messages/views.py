from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SendMessage,SendInvite
from .models import Message

@login_required(login_url='/login')
def my_messages_view(request):
    messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messages/messages.html',{'messages':messages})

@login_required(login_url='/login')
def send_message_view(request,receiver = None):
    if request.method == "POST":
        form = SendMessage(request.POST,user=request.user)
        if form.is_valid():
            form.instance.sender = request.user
            form.save()
            return redirect('home')
    else:
        form = SendMessage(user=request.user,initial={'receiver':receiver,'sender':request.user})
    return render(request,'messages/send_message.html',{'form':form})

def delete_message(request,message):
    msg = get_object_or_404(Message,id = message)
    msg.delete()
    return redirect('messages:my_messages')

def send_invite_view(request):
    if request.method == "POST":
        form = SendInvite(request.POST)
        if form.is_valid():
            form.instance.sender = request.user
            form.instance.title = f'Zaproszenie do drużyny {request.user.player.team}'
            form.instance.description = f'Zostałeś zaproszony przez {request.user} do drużyny {request.user.player.team}'
            form.instance.invited_to = request.user.player.team
            form.save()
            return redirect('home')
    else:
        form = SendInvite()
    return render(request,'messages/send_invite.html',{'form':form})
# Create your views here.

