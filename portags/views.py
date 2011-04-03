from django.shortcuts import render_to_response
from portags.models import Tag, TagsFactory, HtmlFontSizer

def list(request):
    sizer=HtmlFontSizer(50)
    tags=Tag.objects.all()
    setFotSizeTo(sizer, tags)

    return render_to_response("portags/tag_list.html",{"tags" : tags})

def setFotSizeTo(sizer, tags):
    for tag in tags:
        sizer.setSizeTo(tag, tag.numero_busquedas)

def search(request):
    search = request.GET['tags']
    relacionados=None
    for tag in TagsFactory().BuildTagsFromString(search):
        if(relacionados==None):
            relacionados=set(tag.tags_relacionados.all())
        else:
            relacionados=relacionados.intersection(tag.tags_relacionados.all())
        tag.IncrementarNumeroBusquedas()
        tag.save()

    return render_to_response("portags/tag_result.html",{'search':search, 'relacionados':relacionados})
