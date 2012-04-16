from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')
    
def register(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is None:
        user = User.objects.create_user(email, email, password)
        
    login(request, user)
    return redirect('/dashboard/')
    
def render(request, template, bindings={}):
    return render_to_response(template, bindings, context_instance=RequestContext(request))
