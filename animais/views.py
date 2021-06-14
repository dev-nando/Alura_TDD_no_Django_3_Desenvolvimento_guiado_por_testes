from django.shortcuts import render

def index(request):
    context = {'caracteristicas': None}
    return render(request, 'index.html', context)