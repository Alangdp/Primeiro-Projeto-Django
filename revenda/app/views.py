from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def logout(req):
    if req.method == 'GET':
        return render(req, 'users/registro.html')
    if req.user.is_authenticated:
        logout(req)
    return render(req, 'users/registro.html')
    

def homePage(req): 
    return render(req, 'home/home.html')

def userHome(req): 
    if req.user.is_authenticated:
        return render(req, 'users/registro.html')
    return render(req, 'users/registro.html')
    

def userRegister(req): 
    if req.method == 'GET':
        return render(req, 'users/registro.html')    
    
    # Salva os dados do usuario para o banco de dados
    nome = req.POST.get('nome')
    email = req.POST.get('email')
    senha = req.POST.get('senha')

    # Verifica se o usuario já existe no banco de dados via email
    user = User.objects.filter(email=email)
    if user.exists():
        return HttpResponse('Email já cadastrado')
    
    # Se não existir cria o usuario com os dados enviados
    user = User.objects.create_user(username=nome, email=email, password=senha)
    user.save()
    
    # return render(req, 'users/registro.html')
    return render(req, 'users/registro.html')

from django.contrib.auth import authenticate, login

def userLogin(req):
    if req.method == 'GET':
        return render(req, 'users/registro.html')

    email = req.POST.get('email')
    password = req.POST.get('senha')

    print(email, password)
    
    user = authenticate(req, username=email, password=password)

    if user:
        login(req, user)
        return HttpResponse('AUTENTICADO')
    else:
        return render(req, 'users/registro.html')