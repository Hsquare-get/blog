from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from loginapp.models import Users

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')
        try:
            user = Users.objects.get(useremail=useremail)
        except Users.DoesNotExist:
            context = {'error_message':"아이디 또는 비밀번호가 일치하지 않습니다."}
            return render(request, 'login.html', context)
        else:
            if check_password(userpassword, user.userpassword):
                request.session['user'] = user.username
                return redirect('/homeapp/home/')
            else:
                context = {'error_message':"아이디 또는 비밀번호가 일치하지 않습니다."}
                return render(request, 'login.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        userpassword = request.POST.get('password')
        repassword = request.POST.get('repassword')
        if userpassword != repassword:
            error_message = "비밀번호가 일치하지 않습니다"
            context = {'error_message':error_message}
            return render(request, 'register.html', context)
        else:
            users = Users(
                username = username,
                useremail = useremail,
                userpassword = make_password(userpassword)
            )
            users.save()
            return render(request, 'login.html')


def forgot(request):
    return render(request, 'forgot.html')


def pwreset(request):
    return render(request, 'pwreset.html')