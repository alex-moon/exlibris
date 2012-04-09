from django.shortcuts import render_to_response

def home(request):
    bindings = {
        'pagetitle' : 'Borrow, buy, loan and sell books to your fellow readers and meet people',
        'content' : '<article><h1>Welcome!</h1><p><span class="exlibris">exlibris</span> is a community of book-lovers designed\
                     to increase both circulation of books and interaction of individuals. You\'re gonna love this I swear.</p></article>',
    }
    return render_to_response('base.html', bindings)
