from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from webapp.forms import Signupform,Postform,Friendsform,Loginform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View,ListView,CreateView,UpdateView
from django.contrib.auth.models import User
from django.db import transaction
import simplejson as json
from django.forms.models import modelformset_factory
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from webapp.models import Post,Friends
from django.contrib.auth.models import User
@csrf_protect
@login_required
def special(request):
    return HttpResponse("you are login successfully")

@login_required
def user_logout(requets):
    logout(requets)
    return HttpResponseRedirect(reverse('signup'))

def signupview(request):

	signup = Signupform(request.POST or None)
	
	if request.method == "POST":

		user = signup.save()

		user.set_password(user.password)

		user.save()

		return HttpResponseRedirect(reverse('Login_page'))

	return render(request,"signup.html",{'signup':signup})

def user_login(request):

    login_context = Loginform(request.POST or None)

    print(login_context)

    if request.method=='POST':
       
        username = request.POST.get('username')
       
        password = request.POST.get('password')
       
        user = authenticate(username=username,password=password)
       
        if user:
       
            if user.is_active:
       
                login(request,user)
       
                print(request.user)

                return HttpResponseRedirect(reverse('home'))
      
            else:
       
                return HttpResponse("Account not activated")
        else:

            print("someone tried to login but login failure")

            print("Username: {} Password: {} ".format(username,password))

            return HttpResponse("Invalid Login details")
    else:
        
        return render(request,"login.html",{'login':login_context})



def postview(request):

    sharepost = Postform(request.POST or None)

    h= Friendsform(request.POST or None)

    p = User.objects.all()

    if request.method=="POST":

        print(request.POST)

        name = request.POST.get('name')

        print(name)

        if sharepost.is_valid():

            share = sharepost.save(commit=False)

            if 'profile_pic' in request.FILES:

                share.profile_pic = request.FILES['profile_pic']

                share.author = request.user

                share.save()

                k = h.save(commit=False)

                k.home_id = share.id

                k.name = name
                
                k.save()

                return HttpResponseRedirect(reverse('home'))

    return render(request,"sharepost.html",{'share':sharepost})

def edit_postview(request,pk=None):
   
    if request.method=='POST':

        return HttpResponseRedirect(reverse('home'))

    n = request.user
        
    h = Post.objects.get(id=pk)

    k = Postform(request.POST or None, instance = h)
        
    return render(request,"edit_post.html",{'k':k})

def homeview(request):

    n=request.user 

    private = Friends.objects.filter(name=n);

    public = Friends.objects.filter(name="All")

    k = str(n)

    return render(request,"homepage.html",{'private':private,'public':public,'name':k})
    
def deletepost(request,pk=None):

    h = Post.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse('home'))
