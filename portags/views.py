from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
    #recoger los tags y procesarlos
    
    #renderizar la bsuqueda de google
    return render_to_response("portags/tag_result.html")
