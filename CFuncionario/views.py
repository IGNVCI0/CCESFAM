from django.http import HttpResponse
from django.shortcuts import redirect, render
from CFuncionario.models import Usuario
# Create your views here.

def login(request):
    return render(request, 'InicioSesion.html')

def home(request):
    return render(request, 'Home.html')

def contacto(request):
    return render(request, 'Contacto.html')

def navbar(request):
    return render(request, 'navbar.html')




# BLOQUE DE CODIGO CON EL QUE SE GUARDA EL USUARIO 

def guardarUsuario(request):
    v_nombre=request.POST.get('Nombre')
    v_email=request.POST.get('Email')
    v_contraseña=request.POST.get('Contraseña')

    nuevo=Usuario()
    nuevo.Nombre=v_nombre
    nuevo.Email=v_email
    nuevo.Contraseña=v_contraseña

    Usuario.save(nuevo)

    return redirect('/login')


# BLOQUE DE CODIGO CON EL QUE SE VALIDA EL USUARIO LOGEADO

def validarUsuario(request):
    try:
        v_email=request.POST.get('Email')
        v_contraseña=request.POST.get('Contraseña')
        

        usuario=Usuario.objects.get(Contraseña=v_contraseña, Email=v_email)
        
        #crear la sesion y redireccionar
        request.session['Email']=usuario.Email
        #return HttpResponse(v_password + ' ' + v_email)
        return redirect('/home')
        
        
    except Exception as e:
        return HttpResponse(e)
        #return redirect('/')