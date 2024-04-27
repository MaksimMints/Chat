from django.http import HttpResponse
import json
from django.core.cache.backends.locmem import _caches as cache


# список комнат из кэша
def rooms_reader():
    rooms = []
    for key in cache['us']:
        rooms.append(key)
    return rooms


# страница "В начало"
def index(request):
    rooms = rooms_reader()
    return render(request, "index.html", context={'rooms': rooms})


# получить room_name из url
def room(request, room_name):
    room_name = room_name.replace(' ', '_')
    return render(request, "chatroom.html", context={"room_name": room_name})


# обновить roooms из кэша для index.html
def rooms_return(request):
    rooms = rooms_reader()
    jsn = json.dumps(rooms)
    return HttpResponse(jsn)
from django.shortcuts import render


