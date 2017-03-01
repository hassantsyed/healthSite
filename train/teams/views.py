from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def profile(request):
    user = request.user
    return render(request, 'teams/profile.html', {'user':user})
@login_required
def browse(request):
    return render(request, 'teams/browse.html')
