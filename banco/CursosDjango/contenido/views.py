
from django.shortcuts import render, redirect
from .models import Curso
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    contexto = {
        'titulo': 'Bienvenido a Cursos Django',
        'descripcion': 'Este portal ofrece una variedad de cursos para potenciar tus habilidades en programación y bases de datos.'
    }
    return render(request, 'contenido/index.html', contexto)

def cursos(request):
    lista_cursos = Curso.objects.all()
    return render(request, 'contenido/cursos.html', {'cursos': lista_cursos})

def contacto(request):
    cursos = Curso.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        curso_seleccionado = request.POST.get('curso')
        comentarios = request.POST.get('comentarios')

        # Aquí puedes enviar un correo o guardar la información
        # Ejemplo: send_mail(...), se requiere configurar en settings

        return redirect('index')

    return render(request, 'contenido/contacto.html', {'cursos': cursos})
