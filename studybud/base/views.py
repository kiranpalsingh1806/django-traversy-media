from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     { 'id' : 1, 'name' : "Let's learn Python"},
#     { 'id' : 2, 'name' : "Web Development"},
#     { 'id' : 3, 'name' : "Ruby on Rails"},
#     { 'id' : 4, 'name' : "Flask Dev"},
# ]

def home(request) :
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)