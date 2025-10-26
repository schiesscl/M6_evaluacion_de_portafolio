from django.shortcuts import render

def home(request):
    """Vista principal de la aplicación"""
    context = {
        'title': 'Inicio',
        'welcome_message': '¡Bienvenido a la Aplicación Django!'
    }
    return render(request, 'core_p6/home.html', context)

def about(request):
    """Vista de información sobre la aplicación"""
    context = {
        'title': 'Acerca de',
        'description': 'Proyecto Django para Portafolio - Talento Digital'
    }
    return render(request, 'core_p6/about.html', context)
