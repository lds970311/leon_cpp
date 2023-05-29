from django.http import HttpResponse, HttpRequest
from django.template.loader import render_to_string
from django.views.generic import TemplateView


# Create your views here.

def hello_world(request):
    return HttpResponse('hello world')


def world(request: HttpRequest):
    return HttpResponse('world')


def article_list(request, month: int):
    return HttpResponse('article' + str(month))


def render_str(request):
    html = render_to_string('index.html')
    return HttpResponse(html)


class MyView(TemplateView):
    template_name = 'my_view.html'
