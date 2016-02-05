from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_http_methods

def home(request):
    return render(request, 'frontend/home/home.html')

@require_http_methods(["POST"])
def app_login(request):
    if request.method != 'POST' :
        return redirect('home')
    
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None and user.is_active:
        login(request, user)
    else:
        messages.add_message(request, messages.ERROR, "The username and password were incorrect.")
    
    return redirect('home')
    
def app_logout(request):
    logout(request)
    return redirect('home')