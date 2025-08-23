from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message

@login_required
def home(request):
    rooms = ChatRoom.objects.all()

    # Kama user akiingiza room name kwa homepage
    if request.method == "GET" and 'room_name' in request.GET:
        room_name = request.GET.get('room_name')
        return redirect('room', room_name=room_name)

    return render(request, 'chat/home.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    room, created = ChatRoom.objects.get_or_create(name=room_name)

    if request.method == "POST":
        message = request.POST.get('message')
        if message.strip():
            Message.objects.create(room=room, user=request.user, content=message)
        return redirect('room', room_name=room_name)

    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})
