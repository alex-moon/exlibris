from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def home(request):
    bindings = {
        'pagetitle' : 'Borrow, buy, loan and sell books to your fellow readers and meet people',
        'content' : '<article><h1>Welcome!</h1><p><span class="exlibris">exlibris</span> is a community of book-lovers designed\
                     to increase both circulation of books and interaction of individuals. You\'re gonna love this I swear.</p></article>',
        'user' : request.user,
    }
    return render_to_response('base.html', bindings)
    
def register(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is None:
        user = User.objects.create_user(email, email, password)
    authlogin(request, user)
    return redirect('/')
