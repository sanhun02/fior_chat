from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from rooms.models import Room, Msg

def home(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        user = request.user.username
        rooms = Room.objects.all()
        user_rooms = []
        msgs = []

        for room in rooms:
            if room.slug in room.users and user in room.users.get(room.slug) and room not in user_rooms:
                user_rooms.append(room)
                
                if Msg.objects.filter(room=room).exists():
                    msg = Msg.objects.filter(room=room).latest('data_added').content
                    msgs.append((room.slug, msg))
                else:
                    msgs.append((room.slug, ''))
            else:
                user_rooms
    
    if request.method == 'POST':
        room_slug = request.POST['current-room']
        home_room = Room.objects.get(slug=room_slug)
        home_msgs = Msg.objects.filter(room=home_room)
    else:
        if len(user_rooms) != 0:
            home_room = user_rooms[0]
            home_msgs = Msg.objects.filter(room=home_room)
        else:
            home_room = None
            home_msgs = None

    return render(request, 'fior_app/home.html', {'user_rooms' : user_rooms, 'msgs' : msgs, 'home_room' : home_room, 'home_msgs' : home_msgs})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
        else:
            form = SignUpForm()
    else:
        form = SignUpForm()

    return render(request, 'fior_app/signup.html', {'form' : form})

def create_room(request):
    if request.method == 'POST':
        roomName = request.POST['room_name']
        Room.objects.create(name=roomName, slug=roomName.lower())

        return redirect('rooms')

    context = {}
    return render(request, 'fior_app/create_room.html', context)
