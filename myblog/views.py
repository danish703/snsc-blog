from django.shortcuts import HttpResponse,render

def about(request):
    context = {
      'name':"ram kumar shrestha",
       'age':30
    }
    return render(request,'about.html',context)

def contactus(request):
    return HttpResponse("Contact us")
