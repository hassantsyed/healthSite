from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import User
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def loginview(request):
    if request.method =="POST":
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error':'Account credentials are invalid'})
    else:
        return render(request, 'accounts/login.html')

def signup(request):
    User = get_user_model()
    if request.method =="POST":
        if request.POST['password1']==request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username is taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                #user.experience = request.POST['description']
                login(request,user)
                #user.save()
                return redirect('info')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'accounts/signup.html')

def checkUser(request):
    name = request.GET.get('username', None)
    if(User.objects.filter(username=name).exists()):
        return HttpResponse("taken")
    else:
        return HttpResponse("Available")


@login_required
def info(request):
    if request.method =="POST":
        myfile = request.FILES.get("proPic")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        user = request.user
        user.experience = request.POST['experience']
        user.city = request.POST['city']
        user.state = request.POST['state']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        area = {'Personal Trainer':'TRAIN', 'Nutritionist':'NUTRITION' , 'Doctor': 'MD', 'User':'User'}
        temp = request.POST['selection']
        user.pic = filename
        #print(area[temp])
        user.area = area[temp]
        user.save()
        return redirect ('profile')
    else:
        return render(request, 'accounts/info.html', {'experience': request.user.experience})

def logoutview(request):
    logout(request)
    return redirect('login')
