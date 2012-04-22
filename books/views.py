from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from books.models import Book, Edition, Text, Person

def dashboard(request):
    person = Person.objects.get(user=request.user)
    records = person.collections[0].getRecordList()
    return render(request, 'dashboard.html', {'person':person, 'records':records})

def home(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')
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
