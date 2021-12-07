from django.http.response import HttpResponse
from django.shortcuts import render
from.models import data, team

# Create your views here.
def home(request):
    obj=data.objects.all()
    team1=team.objects.all()
    return render(request,'index.html',{'data':obj,'team':team1})




