from django.shortcuts import render
from .models import EventsConfig
# Create your views here.
def home(req):
    events = EventsConfig.objects
    return render(req, "events/home.html", {"params":{"events":events}})