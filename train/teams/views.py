from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import User, Weight, Task, JoinTeam
from django.core import serializers

# Create your views here.
@login_required
def profile(request):
    user = request.user
    peeps = user.group.all()
    peeps = peeps.exclude(area="User")
    tasks = Task.objects.filter(doer=user)
    if user.area == "User":
        return render(request, 'teams/profile.html', {'user':user, 'peeps':peeps, 'provider':False, 'tasks': tasks})
    else:
        reqs = JoinTeam.objects.all()
        return render(request, 'teams/profile.html', {'user':user, 'peeps':peeps, 'provider':True, 'tasks': tasks, 'reqs':reqs})

@login_required
def provider(request):
    user = request.user
    peeps = user.group.all()
    peeps = peeps.filter(area="User")
    return render(request, 'teams/provider.html', {'user':user, 'peeps':peeps})

@login_required
def browse_trainers(request):
    trainers = User.objects.filter(area="TRAIN")
    return render(request, 'teams/browse_trainers.html',{'trainers':trainers})

@login_required
def person(request, username):
    p = get_object_or_404(User, username=username)
    user = request.user
    if request.method == "POST":
        if (user.group.all().filter(username=username)):
            user.group.remove(User.objects.filter(username=username)[0])
            user.save()
        else:
            user.group.add(User.objects.filter(username=username)[0])
            user.save()
    if (user.group.all().filter(username=username)):
        b = True
    else:
        b = False
    return render(request, 'teams/person.html', {'person':p,'button':b})

@login_required
def browse_doctors(request):
    doctors = User.objects.filter(area="MD")
    return render(request, 'teams/browse_doctors.html',{'doctors':doctors})

@login_required
def browse_nutritionists(request):
    nutritionists = User.objects.filter(area="NUTRITION")
    return render(request, 'teams/browse_nutritionists.html',{'nutritionists':nutritionists})

def weight(request):
    #json_serializer = serializers.get_serializer("json")()
    #weight = json_serializer.serialize(Weight.objects.filter(person = request.user), ensure_ascii=False)
    user = request.user
    weight = Weight.objects.filter(person = user)
    dates = []
    pounds = []
    x = 1
    for w in weight:
        pounds.append(w.pds)
        dates.append(x)
        x = x+1
    return render(request, "teams/weight.html", {'weight':pounds, 'date':dates})

def addWeight(request):
    user = request.user
    amount = request.GET.get('weight')
    weight = Weight.objects.create(pds = amount, person = user)
    return HttpResponse("")

def deleteWeight(request):
    user = request.user
    weights = Weight.objects.filter(person = user)
    last = weights[len(weights)-1]
    last.delete()
    return HttpResponse("")

def addTask(request):
    provider = request.user
    taker = User.objects.filter(id=request.GET.get("person"))
    stuff = request.GET.get("info")
    task = Task.objects.create(info = stuff, giver=provider, doer=taker[0])
    return HttpResponse("")

def deleteTask(request):
    taker = request.user
    t = Task.objects.filter(id = request.GET.get('key'))
    t[0].delete()
    return HttpResponse("")
