from django.http import HttpResponse
from django.shortcuts import render_to_response
from portags.models import Tag, TagsFactory, HtmlFontSizer

def list(request):
    sizer=HtmlFontSizer(50)
    tags=Tag.objects.all()
    for tag in tags:
        sizer.setSizeTo(tag,tag.numero_busquedas)

    return render_to_response("portags/tag_list.html",{"tags" : tags})

def search(request):
    print request.GET['tags']
    for tag in TagsFactory().BuildTagsFromString(request.GET['tags']):
        tag.IncrementarNumeroBusquedas()
        tag.save()

    return render_to_response("portags/tag_result.html",{'tag':request.GET['tags'], 'tags':tag.tags_relacionados})
