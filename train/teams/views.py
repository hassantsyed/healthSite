from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import User
# Create your views here.
@login_required
def profile(request):
    user = request.user
    peeps = user.group.all()
    peeps = peeps.exclude(area="User")
    return render(request, 'teams/profile.html', {'user':user, 'peeps':peeps})
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
            print('need to delete relationship')
        else:
            user.group.add(User.objects.filter(username=username)[0])
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
