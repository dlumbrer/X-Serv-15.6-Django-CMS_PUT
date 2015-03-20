from django.shortcuts import render
from models import Pages
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def mostrar(request, recurso):
    if request.method == "GET":
        #MUESTRO DE LA BD
        try:
            fila = Pages.objects.get(name=recurso)
            return HttpResponse(request.method + " " + str(fila.id) + " " + fila.name + " " + fila.page)
        except Pages.DoesNotExist:
            return HttpResponseNotFound("Page not found: " + recurso)
    elif request.method == "PUT":
        #GUARDO EN LA BD
        p = Pages(name=recurso, page=request.body)
        p.save()
        return HttpResponse("guardada pagina, haz un get para comprobar")
