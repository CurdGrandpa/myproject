from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


#from django.http import HttpResponse
#def homePageView(request):
#    return HttpResponse('Hello, World!')
