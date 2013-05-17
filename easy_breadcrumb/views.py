from django.http import HttpResponse
from django.template import loader, RequestContext

def home(request):
    t = loader.get_template('demo.html')
    return HttpResponse(t.render(RequestContext(request, {})))


def section(request):
    t = loader.get_template('section.html')
    return HttpResponse(t.render(RequestContext(request, {})))


def sub_section(request):
    t = loader.get_template('sub-section.html')
    return HttpResponse(t.render(RequestContext(request, {})))


#     return HttpResponse('<h1>hai</h1>')
