from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    if 'user' in request.session:
        context = {'username' : request.session['user']}
    return render(request, 'home.html', context)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return render(request, 'home.html')