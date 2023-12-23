from django.shortcuts import render,redirect
from .forms import LoginForm,SignupForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
# Create your views here.
def sign_up(request):
    if request.method =='GET':
        form=SignupForm()
        return render(request,'users/signup.html',{'form':form})

    elif request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']


            if User.objects.filter(username=username).first():
                messages.error(request,"This username is already taken")
                return redirect('signup')
                
            myuser = User.objects.create_user(username,email,password)
            myuser.last_name=lastname
            myuser.first_name=firstname
            # user=authenticate(username=username,password=password)

            myuser.save()
            # user.save()

            messages.success(request,"Your Account has been successfully created or some diff error")
            # messages.success(request,f"{myuser.username}  {myuser.password}")

        return redirect('login')

def sign_in(request):
    if request.method =='GET':
        form=LoginForm()
        return render(request,'users/login.html',{'form':form})

    elif request.method=='POST':
        form =LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None: 
                login(request,user)
                messages.success(request,f'Successfully Logged In as {username}')
                return redirect('index')

        messages.error(request,f'Invalid Username or Password')
        # messages.success(request,f"{user}")

        return render(request,'users/login.html',{'form':form})

def posts(request):
    return render(request,'users/posts.html')

def index(request):
    return render(request,'users/index.html')

def sign_out(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('index')
