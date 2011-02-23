from django.http import HttpResponse

def search(request,tags):
   return HttpResponse(tags)
