from django.shortcuts import render
from .models import ChatRoom, Message

def home(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})

def room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})
