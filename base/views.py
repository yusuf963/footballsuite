from django.shortcuts import render

def home(req):
    return render(req, 'base.html')

def room(req):
    return render(req, '_partials/_nav.html')

def news(req):
    return HttpResponse('this is the news page')