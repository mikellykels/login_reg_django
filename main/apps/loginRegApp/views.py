from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def index(request):
    if not 'errors' in request.session:
        request.session['errors'] = []
    return render(request, 'loginRegApp/index.html')

def create(request):
    if request.method == "POST":
        result = User.UserManager.register(email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], confirm_pw=request.POST['confirm_pw'])
        if result[0]:
            request.session['first_name'] = result[1].first_name
            return redirect('/success')
        else:
            request.session['errors'] = result[1]
            return redirect('/')
    else:
        return redirect ('/')

def login(request):
    if request.method == "POST":
        result = User.UserManager.validateLogin(request)
        if result[0]:
            request.session['first_name'] = result[1].first_name
            return redirect('/success')
        else:
            request.session['errors'] = result[1]
            return redirect('/')

def success(request):
    request.session.pop('errors')
    user = User.UserManager.all()
    return render (request, 'loginRegApp/success.html', {'first_name': request.session.get('first_name'), 'last_name': request.session.get('last_name'), 'your_email': request.session.get('email')})

def logout(request):
    request.session.pop('first_name')
    return redirect('/')
