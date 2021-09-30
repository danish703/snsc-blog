from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Category
from blog.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login

def home(request):
    context = {
        'post':Post.objects.all()[::-1],#SELECT * FROM post;
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

def detailsPage(request,id):
    p = get_object_or_404(Post,id=id)#Post.objects.get(pk=id) #select * from post where id=
    context = {
        'post':p
    }
    return render(request,'details.html',context)

def deletePost(request,id):
    p = get_object_or_404(Post,id=id)
    p.delete()
    return redirect('home')

def createPost(request):
    if request.method=='POST':
        t = request.POST['title']
        i = request.FILES['image']
        c = request.POST['content']
        cat = request.POST['category']
        p = Post(title=t,image=i,content=c,category_id=cat)
        p.save() #INSERT ......
        return redirect('home')
    else:
        c = Category.objects.all()
        context = {
            'category': c
        }
        return render(request, 'createpost.html', context)

def createPostByDjangoForm(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form':form
    }
    return render(request,'createpost2.html',context)


def updateData(request,id):
    p = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=p)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
             'form':form
               }
    return render(request,'edit.html',context)

@login_required(login_url='signin')
def dashboard(reqeust):
    return render(reqeust, 'dashboard.html')


def signin(request):
    if request.method=='POST':
        u = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=u,password=password) #user object other None
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,"username or password does not match")
            return redirect('signin')

    return render(request,'login.html')


def signup(request):
    context = {}
    if request.method=='POST':
        username = request.POST['username']
        name = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        context.update({
            'username':username,
            'name':name,
            'lname':lname,
            'email':email
        })
        if(len(username)==0):
            messages.add_message(request,messages.ERROR,"username can not empty")
            return redirect('signup')
        if password==password2:
            u = User(username=username,first_name=name,last_name=lname,email=email)
            u.set_password(password)
            try:
                u.save()
                messages.add_message(request,messages.SUCCESS,"Signup successfull")
                return redirect('signin')
            except Exception as e:
                messages.add_message(request,messages.ERROR,e)
                return render(request, 'signup.html', context)
        else:
            messages.add_message(request,messages.ERROR,"Password failed")
            return render(request, 'signup.html', context)

    return render(request,'signup.html',context)


def signout(request):
    logout(request)
    return redirect('signin')