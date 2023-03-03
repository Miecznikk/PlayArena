from django.shortcuts import render

# Create your views here.
def stadium_occupied_view(request,opposing_captain_id):
    return render(request,'errors/stadium_occupied.html',{'opposing_captain':opposing_captain_id})
