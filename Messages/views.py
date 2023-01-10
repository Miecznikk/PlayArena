from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SendMessage,SendInvite,SendChallenge
from .models import Message,Invite

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

def accept_invite(request,message):
    msg = get_object_or_404(Invite,id = message)
    if request.user.player.team is None:
        request.user.player.team = msg.invited_to
        request.user.player.save()
        msg.delete()
    return redirect('messages:my_messages')

def send_challenge(request,challenged_team = None):
    if request.method == "POST":
        form = SendChallenge(request.POST,team = request.user.player.team)
        if form.is_valid():
            form.instance.sender = request.user
            form.instance.challenging_team = request.user.player.team
            cd = form.cleaned_data
            team = cd.get('challenged_team')
            form.instance.receiver = team.get_captain()
            form.instance.description = f'Rzucono ci wyzwanie od drużyny {request.user.player.team} dnia' \
                                        f'{cd.get("date")} na boisku {cd.get("stadium")}'
            form.save()
            return redirect('home')
    else:
        form = SendChallenge(team = request.user.player.team,initial={'challenged_team':challenged_team})
    return render(request,'messages/send_challenge.html',{'form':form})
# Create your views here.

