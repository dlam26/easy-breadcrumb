from django.http import HttpResponse
from django.template import loader, Template, Context


def home(request):
    t = loader.get_template('demo.html')
    c = Context({'asdf': 1})
    return HttpResponse(t.render(c))


def section(request):
    t = loader.get_template('section.html')
    c = Context({'asdf': 1})
    return HttpResponse(t.render(c))


def sub_section(request):
    t = loader.get_template('sub-section.html')
    c = Context({'asdf': 1})
    return HttpResponse(t.render(c))


#     return HttpResponse('<h1>hai</h1>')
