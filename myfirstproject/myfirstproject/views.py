from django.http import HttpResponse
from django.shortcuts import render

def about(req):
    return render(req, "index.html", {'name':"andrey"})
def reverse(req):
    params = req.GET["usertext"]
    return render(req, "reverse.html", {"params":params})