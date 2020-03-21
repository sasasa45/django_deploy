from django.shortcuts import render
from app.forms import UserDataForm, UserForm, TrainForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'app/index.html')
def registration (request):
    chacker=False
    if request.method=='POST':
        userform=UserForm(data=request.POST)
        dataform=UserDataForm(data=request.POST)

        if userform.is_valid() and dataform.is_valid():

            user=userform.save()
            user.set_password(user.password)
            user.save()

            data=dataform.save(commit=False)
            data.user=user
            if 'picture' in request.FILES:
                print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
                data.picture=request.FILES['picture']
            data.save()

            chacker=True
        else:
            print(userform.errors,dataform.errors)
    else:
        userform=UserForm()
        dataform=UserDataForm()
    return render(request,'app/registration.html',{'chacker':chacker,
                                                    'userform':userform,
                                                    'dataform':dataform,
                                                                    })
def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                # return index(request)
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Invalidksjndfkjnsd')
    else:
        return render(request,'app/login.html')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
@login_required
def special(request):
    return HttpResponse("you are")
def fnickname(request):
    if request.method=="POST":
        trainform=TrainForm(request.POST)
        if trainform.is_valid:
            train=trainform.save(commit=False)
            print(request.POST.get)
            train.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('fuck')
    else:
        trainform=TrainForm( )
    return render(request,'app/nickname.html',{'trainform':trainform,})
