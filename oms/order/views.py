from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Order

# Create your views here.
def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                print('Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                print('email taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('login')
        else:
            print('password not matching')
            messages.info(request, 'password not matching')
            return redirect('signup')
        return redirect('/')

    return render(request, "signup.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("main")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, "login.html")

def main(request):
    orders = Order.objects.all()
    return render(request, "main.html", {'orders': orders})

