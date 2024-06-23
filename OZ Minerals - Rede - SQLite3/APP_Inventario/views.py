from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')  # Redirecione para a página de administração após o login
        else:
            # Retorne uma mensagem de erro se a autenticação falhar
            return render(request, 'APP_Inventario/login.html', {'error_message': 'Usuário ou senha incorretos.'})
    else:
        return render(request, 'APP_Inventario/login.html')

@login_required
def index_view(request):
    context = {
        'username': request.user.username,
        'email': request.user.email,
    }
    return render(request, 'APP_Inventario/index.html', context)
