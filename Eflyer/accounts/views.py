from django.shortcuts import redirect, render
from django.http import  HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required



def usr_reg(request):
    if request.method == 'POST':
        usernam = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(username = usernam,first_name = first_name , last_name= last_name , email = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)
    

    return render(request, 'signup.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
                
            users = authenticate(request,username=email,password=password)
            print(users)
            if users is not None:
                print("login")
                login(request,users)
                # messages.success(request,'Account loged in')
                return redirect('/')
            else:
                print('wrong')
                messages.info(request,'username or password incorrect')
                
                
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')