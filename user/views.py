from email.headerregistry import Group
from django.shortcuts import redirect, render
from flask import render_template
from psutil import users
from .forms import userRegister
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect




@csrf_protect
def Register(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    if request.method == "POST":
        form = userRegister(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            #print('success')
            return redirect('/login')
        #print('error')
    form = userRegister()
    context ={'form':form}
    return render(request, 'userTemplates/userReg.html', context)



