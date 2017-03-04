from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from accounts.models import User
# Create your views here.
@login_required
def profile(request):
    user = request.user
    return render(request, 'teams/profile.html', {'user':user})
@login_required
def browse_trainers(request):
    trainers = User.objects.filter(area="TRAIN")
    return render(request, 'teams/browse_trainers.html',{'trainers':trainers})
@login_required
def person(request, username):
    p = get_object_or_404(User, username=username)
    return render(request, 'teams/person.html', {'person':p})

@login_required
def browse_doctors(request):
    doctors = User.objects.filter(area="MD")
    return render(request, 'teams/browse_doctors.html',{'doctors':doctors})

@login_required
def browse_nutritionists(request):
    nutritionists = User.objects.filter(area="NUTRITION")
    return render(request, 'teams/browse_nutritionists.html',{'nutritionists':nutritionists})
