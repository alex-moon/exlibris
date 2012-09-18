from django.shortcuts import render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from books.models import Book, Edition, Text, Person
from books import forms

import json

def dashboard(request):
    person = Person.objects.get(user=request.user)
    return render(request, 'dashboard.html', {'person':person})

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
    
def add_book(request):
    # generate form and pass it to add yeeeeeaaaaah!
    return render(request, 'books/add.html')

def edit_book(request, book_id):
    # book = Book.objects.get(id=book_id)
    person = Person.objects.raw_query({'collections.books.id':book_id})[0]
    book_to_edit = None
    for collection in person.collections:
        for book in collection.books:
            if book.id == book_id:
                book_to_edit = book
                break
        if book_to_edit is not None:
            break

    form = forms.BookForm(request.POST, instance=book_to_edit)
    return render(request, 'books/edit.html', {'form' : form })
    
def ajaxSearch(request, model, field):
    options = {
        'text' : {
            'title' : textTitleSearch
        }
    }
    query = request.GET['query']
    if model in options:
        if field in options[model]:
            return render(request, 'ajax/search.html', {'content' : options[model][field](query) })
    return HttpResponseBadRequest()

def textTitleSearch(query):
    # todo: split query into words and OR these - something more sophisticated would be even better
    # doesn't mongo have a full text search for this?
    results = Text.objects.filter(title__iregex=query)
    suggestions = [result.title for result in results]
    data = [result.id for result in results]
    return "{query:'%s', suggestions:%s, data:%s}" % (query, json.dumps(suggestions), json.dumps(data))
    
def render(request, template, bindings={}):
    return render_to_response(template, bindings, context_instance=RequestContext(request))
