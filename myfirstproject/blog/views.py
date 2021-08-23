from django.shortcuts import render
# from .models import EventsConfig
# Create your views here.
def show(req):
    return render(req, 'blog/posts.html', {"params":{"events":"events"}})