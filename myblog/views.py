from django.shortcuts import render
from blog.models import Post

def home(request):
    context = {
        'post':Post.objects.all(),#SELECT * FROM post;
    }
    return render(request,'home.html',context)


def about(request):
    context = {
      'name':"ram kumar shrestha",
       'age':30
    }
    return render(request,'about.html',context)

def contactus(request):
    return render(request,'contact.html')
