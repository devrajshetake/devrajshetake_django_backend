from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_User, logout as logout_User

def register(request):
    

    if request.method == 'POST':

        err_lst = []

        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        hashed_password = make_password(password1)

        users = User.objects.all()
        members = Member.objects.all()

        if(password1 != password2):
            err_lst.append("Passwords not Matching!")
        # if User.filter(username).exists():
        #     err_lst.append("This Username is already taken.")
        for user in users:
            if user.username == username:
              err_lst.append("This Username is already taken.")  
              break
        for user in users:
            if user.email == email:
              err_lst.append("This Email is Already linked to an existing Username.")
              break
        for member in members:
            print(member.phone)
            print(phone)
            if member.phone == int(phone):
              err_lst.append("This Phone Number is Already linked to an existing Username.")
              break
        
        

        
        if len(err_lst) == 0:
            u1 = User(username = username, first_name = fname, last_name = lname, email= email, password = hashed_password)
            u1.save()
            profile = Member(user = u1, phone =phone, gender = gender )       
            profile.save()
            print("User created successfully")
            return render (request, 'users/register.html', {'success_message': "Registration Succsessful!"})
        else:
            return render(request, 'users/register.html', {'err_lst': err_lst})

    else:
        return render (request, 'users/register.html')


def home (request):
    if not request.user.is_authenticated:
        return render(request, 'users/home.html', {'isLoggedIn': False})
    else:
        return render(request, 'users/home.html', {'isLoggedIn': True})
            

def login(request):
    if request.method == 'POST':
        username = request.POST['username']    
        password = request.POST['password']
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login_User(request, user)
            return redirect(reverse("home"))
        else:
            return render(request, 'users/login.html', {'message': "Invalid Credentials!"})
    
    return render(request, 'users/login.html')

def logout(request):
    logout_User(request)
    return redirect(reverse("register"))

def search(request):
    if request.method == 'POST':
        email = request.POST['email']
        usersearched = User.objects.get(email__exact = email)
        member = Member.objects.get(user = usersearched)
        context = {'usersearched':usersearched, 'member':member}
        print(usersearched.first_name)
        return render(request, 'users/search.html', context)

        
    return render(request, 'users/search.html')
