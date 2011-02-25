from django.http import HttpResponse
from django.shortcuts import render_to_response
from portags.models import Tag

def search(request):
    #recoger los tags y procesarlos
    tags=request.GET['tags']
    lista_tag=tags.split()
    try:
        tag=Tag.objects.get(nombre=lista_tag[0])
        tag.numero_busquedas+=1
    except Tag.DoesNotExist:
        tag=Tag(nombre=lista_tag[0],numero_busquedas=1)

    tag.save()
    #renderizar la bsuqueda de google
    return render_to_response("portags/tag_result.html",{'tag':tag.nombre})
