from django.shortcuts import render,redirect
from .forms import RegisterationForm,PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    posts = Post.objects.using('default_db').all()
    return render(request, 'home.html' ,{'posts': posts})


def RegisterUser(request):  # sourcery skip: extract-method
    if request.method == 'GET':
        form = RegisterationForm()
    else:
        form = RegisterationForm(request.POST)
        if form.is_valid():
            data = {
                'username': form.cleaned_data['username'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email']
            }
            password = form.cleaned_data['password1']
            newuser = User.objects.using('default_db').create(**data)
            newuser.set_password(password)
            newuser.save(using ='default_db')
            messages.success(request,'User registered successfully ')
            return redirect('login')

    return render(request,'register.html', {'form':form})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.using('default_db').filter(user=request.user)
    totalpost = len(list(posts))
    return render(request, 'dashboard.html' ,{'Posts':posts,'totalPost':totalpost})
    

def AddPost(request):  # sourcery skip: extract-method
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'GET':
        form = PostForm()
        
    else:
        form = PostForm(request.POST)
        if form.is_valid():            
            user = request.user
            
            text = form.cleaned_data['text']
            posts = Post(user = user, text = text)
            posts.save(using='default_db')
            messages.success(request , 'Post added successfully')

            return redirect('dashboard')
    return render(request, 'addpost.html', {'form': form,'title':'Add'})


def UpdatePost(request,id):
    if not request.user.is_authenticated:
        return redirect('login')

    blogpost = Post.objects.using('default_db').get(pk = id)
    if request.method == 'GET':
        form = PostForm(instance=blogpost)
        
    else:
        form = PostForm(request.POST,instance=blogpost)
        if form.is_valid():
            blogpost.text = form.cleaned_data['text']
            blogpost.save(using='default_db')
            messages.success(request , 'Post updated successfully')
            return redirect('dashboard')
    return render(request, 'addpost.html', {'form': form , 'title':'Update'})

def DeletePost(request,id ):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST' :
        blogpost = Post.objects.using('default_db').get(pk = id)
        blogpost.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('dashboard')
