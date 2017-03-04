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
def browse(request):
    return render(request, 'teams/browse.html')
@login_required
def person(request, username):
    p = get_object_or_404(User, username=username)
    return render(request, 'teams/person.html', {'person':p})
