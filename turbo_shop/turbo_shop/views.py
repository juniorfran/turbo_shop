from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from users.models import User
from products.models import Product

from .forms import RegistroForm

"""
def index(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'index.html', {
        'message':'Lista de productos',
        'title':'Productos',
        'productos': products
    })
    pass

"""

def login_view (request):
    if request.user.is_authenticated :
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password) #none

        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect('index')
            pass
        else :
            messages.error(request, "Usuario o contraseña no validos")

    return render(request, 'users/login.html', {
        'title':'Login'
    })
    pass

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosa mente.')
    return redirect('login')
    pass

def registro(request):
    if request.user.is_authenticated :
        return redirect('index')

    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        ##name = form.cleaned_data.get('name') #cleaned_data es un diccionario
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)

        if user :
            login(request, user)
            messages.success(request,"Usuario creado exitosamente")
            return redirect('index')

        pass


    return render(request, 'users/registro.html', {
        'title': 'Registro',
        'form' : form
    })