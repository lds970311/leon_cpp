from django.http import HttpResponse, HttpRequest


# Create your views here.


def index(request: HttpRequest):
    return HttpResponse('index')
