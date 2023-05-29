from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.

def index(request: HttpRequest):
    username = 'leon'
    age = 21

    l = [
        {'name': '妲己', 'job': '法师', 'times': 32},
        {'name': '王昭君', 'job': '法师', 'times': 21},
        {'name': '李白', 'job': '刺客', 'times': 100},
    ]

    return render(request, 'tmp.html', {
        'username': username,
        'age': age,
        'heros': l
    })
