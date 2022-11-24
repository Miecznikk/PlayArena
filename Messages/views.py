from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SendMessage

@login_required(login_url='/login')
def send_message_view(request,receiver = None):
    if request.method == "POST":
        form = SendMessage(request.POST,user=request.user)
        if form.is_valid():
            form.instance.sender = request.user
            form.save()
            return redirect('playarena:home')
    else:
        form = SendMessage(user=request.user,initial={'receiver':receiver,'sender':request.user})
    return render(request,'messages/send_message.html',{'form':form})

# Create your views here.
