from django.shortcuts import render

def inicio(request):
    return render(request, 'web/inicio.html')

def quien_soy(request):
    return render(request, 'web/quien_soy.html')

def contacto(request):
    return render(request, 'web/contacto.html')
