from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect
# Create your views here.
def register(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,'Name already exists')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')

            elif User.objects.filter(password=password).exists():
                messages.info(request,'password already exists')
                return redirect('register')

            else:
                user=User.objects.create_user(username=name,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print('user created')
                messages.info(request,'user created')
                return redirect('login')
        else:
            print('password did not match.')
            messages.info(request,'password did not match')
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        user=auth.authenticate(username=username,password=password)
        if password==cpassword:
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,'Invalid credential')
                return redirect('login')
        else:
            messages.info(request,'passsword did not match')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')