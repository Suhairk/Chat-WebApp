from django.shortcuts import redirect, render
from flask import render_template
from psutil import users
from django.contrib.auth.forms import AuthenticationForm
from sympy import re
from .models import Group, Message,privateMessage
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import query,Q
#home section----------------------------------------------------------
@login_required
def home(request):
    if request.user.is_authenticated:
        groupinfo = Group.objects.all()
        currentUser = request.user.username
        users =  User.objects.exclude(username=request.user.username)
        context = {'userinfo':users,
               'groupinfo':groupinfo,
               'currentUser':currentUser
               }
        return render(request, 'chathome/home.html',context)
    
#-----------------------------Group chat-----------------------------

@login_required
def group(request, group):
    username = request.GET.get('username')
    currentUser = request.user.username
    group_details = Group.objects.get(name=group)
    users =  User.objects.exclude(username=request.user.username)

    getActiveUserfromMessage = Message.objects.filter(
                            group_name = group_details.id
                            ).order_by('date')
    
    userslist = []
    for i in getActiveUserfromMessage:
        userslist.append(i.user_name)
    UniquegetActiveUserfromMessage = list(set(userslist))
    return render(request , 'chathome/group.html',{
        'group':group,
        'group_details':group_details,
        'Activeusers':UniquegetActiveUserfromMessage,
    })
    
#-----------------------------Check existing group and create-----------------------------

@login_required
@csrf_protect
def check(request):
    group = request.POST['group_name']
    currentUser = request.user.username
    if Group.objects.filter(name = group).exists():
        return redirect('/user/'+group+'/?username='+currentUser)
    else:
        new_group = Group.objects.create(name = group)
        new_group.save()
        return redirect('/user/'+group+'/?username='+currentUser)  
       
from django.http import HttpResponse, JsonResponse
import json

#-----------------------------Send Group chat-----------------------------

@csrf_protect
def send(request):
    if request.method =='POST':
        data = json.loads(request.body.decode("utf-8"))
        currentUser =data['username']
        group_id = data['group_id']
        message = data['message']
        createMessage = Message.objects.create(message_text=message, user_name=currentUser,group_name=group_id)
        createMessage.save()
        return HttpResponse("data added")   
    
#-----------------------------Display Group chat-----------------------------

def getMessages(request, group):
    group_details = Group.objects.get(name=group) 
    messages = Message.objects.filter(group_name = group_details.id)
    return JsonResponse({"messages":list(messages.values())})


#-----------------------------Private  chat-----------------------------

def private_chat(request,sender,receiver):
    sender = User.objects.get(username = sender)
    receiver = User.objects.get(username = receiver)
    context = {
        'sender':sender,
        'receiver':receiver
    }
    return render(request,'chathome/privatechat.html',context)

#-----------------------------send Private chat  messages -----------------------------


def sendPrivateMsg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        sender = User.objects.get(username = request.user.username)
        receiver = User.objects.get(username =data['receiver'])
        messages = data['messages']
        createPrivateMsg = privateMessage.objects.create(
            sender = sender,
            receiver = receiver,
            message_text = messages
        )
        createPrivateMsg.save()
        return HttpResponse("data get")
        
#-----------------------------display Private chat  messages -----------------------------

def getPrivateMessages(request, sender, receiver):
    sender = User.objects.get(username=sender)
    receiver = User.objects.get(username = receiver)
    messages = privateMessage.objects.filter(sender = sender , receiver = receiver ) | privateMessage.objects.filter(sender= receiver , receiver = sender ) 
    return JsonResponse({"messages":list(messages.values())})




         
         
         
         
 