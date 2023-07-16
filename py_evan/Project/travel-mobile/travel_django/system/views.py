from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Slider


# Create your views here.
def slider_list(request: HttpRequest):
    data = {
        'meta': {},
        'objects': []
    }
    queryset = Slider.objects.filter(is_valid=True)
    for item in queryset:
        data['objects'].append({
            'id': item.id,
            'img_url': item.img.url,
            'target_url': item.target_url,
            'name': item.name
        })
    return JsonResponse(data)
