from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import RegisterForm,ProfileEditForm
from .models import Position,Player,App_User,Team
from django.contrib.auth import login, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.db.models.signals import post_save
from django.dispatch import receiver
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Link aktywacyjny został wysłany na email'
            message = render_to_string('acc_active_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[to_email])
            email.send()
            return HttpResponse('Potwierdź swój email aby dokończyć rejestrację')
    else:
        form = RegisterForm()

    return render(request,'registration/sign_up.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        return HttpResponse('Dziękujemy, twoje konto zostało aktywowane')
    else:
        return HttpResponse('Link aktywacyjny jest niepoprawny!')

def home_view(request):
    return render(request,'home.html',{})

def player_detail(request,id):  
    player = get_object_or_404(Player,id=id)
    return render(request,'players/player_detail.html',{'player':player})

def player_ranking(request):
    players = sorted(Player.objects.all(),key=lambda x:x.get_scored_goals(),reverse=True)
    context = {
        'players':players
    }
    return render(request,'players/player_ranking.html',context=context)

@login_required(login_url='/login')
def update_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,request.FILES,instance=request.user.player)
        if form.is_valid():
            request.user.first_name = form.cleaned_data.get('first_name')
            request.user.last_name = form.cleaned_data.get('last_name')
            request.user.save()
            form.save()
            return redirect('home')

    else:
        player = get_object_or_404(Player,id = request.user.player.id)
        initial_player_values = {
            'first_name':player.first_name,
            'second_name':player.second_name,
            'last_name':player.last_name,
            'shirt_number':player.shirt_number,
            'image':player.image
        }
        form = ProfileEditForm(initial=initial_player_values)
    return render(request,'players/profile.html',{'form':form})

def best_of_all(request):
    players = sorted(Player.objects.all(), key=lambda x: x.get_scored_goals(), reverse=True)[0:3]
    teams = sorted(Team.objects.all(), key=lambda x: x.get_points(), reverse=True)[0:3]
    context = {
        'players': players,
        'teams':teams
    }
    return render(request,'best_of_all.html', context=context)
##DONE## VIEW WITH ARRAY OF BEST TEAMS AND PLAYERS FOR REWARDS#### ## TO CHECK !!!!