from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Msg
from django.contrib.auth.models import User


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    username = request.user.username
    room = Room.objects.get(slug=slug)
    msgs = Msg.objects.filter(room=room)

    if len(room.users) == 0:
        room.users[room.slug] = []
        room.users.get(room.slug).append(username)

    elif room.slug not in room.users:
        room.users[room.slug] = []
        room.users.get(room.slug).append(username)

    elif username not in room.users[room.slug]:
        room.users.get(room.slug).append(username)

    return render(request, 'rooms/room.html', {'room': room, 'msgs': msgs})