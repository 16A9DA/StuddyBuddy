from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Rooms,Topic,Message
from .forms import RoomForm,MessageForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def loginRegister(request):
   page = 'login'
   if request.user.is_authenticated:
      return redirect('Home')
   if request.method == 'POST':
      username = request.POST.get('username').lower()
      password = request.POST.get('password')
      try:
         user = User.objects.get(username=username)
      except:
         messages.error(request,"Username does exit")

      
      user = authenticate(request,username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('Home')
      else:
         messages.error(request, "Username or Password does not exist.")

   content = {'page':page}
   return render(request,'base/loginRegister.html',content)


def logoutUser(request):
   logout(request)
   return redirect('login')


def registerUser(request):
   form = UserCreationForm
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.username = user.username.lower()
         user.save()
         login(request,user)
         return redirect('Home')
      else:
         messages.error(request,'An error occured during registration, try again !')
   return render(request,'base/loginRegister.html',{"form":form})


def home(request):
  q = request.GET.get('q','')
  rooms = Rooms.objects.filter(Q(topic__name__icontains=q ) |  Q(name__icontains=q))
  topics = Topic.objects.all()
  room_count = rooms.count()
  content = {"rooms":rooms,
             "topics":topics,
             "room_count":room_count
             }
  
  return render(request,'base/index.html',content)




def room(request,pk):
    rooms = Rooms.objects.get(id=pk)
    room_messages = rooms.message_set.all().order_by('-created')
    particpants = rooms.participant.all()
    if request.method == "POST":
       room_messages = Message.objects.create(
          user = request.user,
          room = rooms,
          body = request.POST.get('body')

       )
       rooms.participant.add(request.user)
       return redirect('room',pk=rooms.id)
    

    content =   {"rooms":rooms,"messages":room_messages,"participants":particpants}
    return render(request,'base/room.html',content)


@login_required(login_url='login')
def create_room(request):
    topics = Topic.objects.all()

    if request.method == "POST":
        new_topic = request.POST.get('new_topic', '').strip()
        selected_topic = request.POST.get('topic', '').strip()

        topic_name = new_topic if new_topic else selected_topic

        if topic_name:
            topic, created = Topic.objects.get_or_create(name=topic_name)
            Rooms.objects.create(
                host=request.user,
                topic=topic,
                name=request.POST.get('name'),
                description=request.POST.get('description')
            )
            return redirect('Home') 

    context = {'topics': topics, 'type': 'room'}
    return render(request, 'base/forms.html', context)


@login_required(login_url='login')
def update_room(request,pk):
   room = Rooms.objects.get(id = pk)
   form = RoomForm(instance=room)
   topic = Topic.objects.all()

   if request.method == "POST":
      topic_name = request.POST.get('topic')
      topic, created = Topic.objects.get_or_create(name=topic_name)
      room.name = request.POST.get('name')
      room.topic = topic
      room.description = request.POST.get('description')
      room.save()
      return redirect('Home')
   
   content = {"form":form,'topics':topic,"room":room}
   return render(request,'base/forms.html',content )


@login_required(login_url='login')
def delete_room(request,pk):
   room = Rooms.objects.get(id=pk)

   if request.method == 'POST':
      topic = room.topic
      room.delete()
      if topic and not Rooms.objects.filter(topic=topic).exists():
         topic.delete()

      return redirect('Home')
   return render(request,"base/delete.html",{'obj':room})



@login_required(login_url='login')
def delete_message(request,pk):
   message  = Message.objects.get(id=pk)

   if request.user != message.user :
      return HttpResponse("You are not allowed")
   
   if request.method == 'POST':
      message.delete()
      return redirect('Home')
   return render(request,"base/delete.html",{'obj':message})



@login_required(login_url='login')
def update_message(request,pk):
   type = 'message'
   message = Message.objects.get(id = pk)
   if request.user != message.user :
      return HttpResponse("You are not allowed")
   form = MessageForm(instance=message)

   if request.method == "POST":
      form = MessageForm(request.POST,instance=message)
      if form.is_valid():
         form.save()
         return redirect('Home')
         
   content = {"form":form,"type":type}
   return render(request,'base/forms.html',content)



def user_profile(request,username):
   profile_user = User.objects.get(username=username)
   room = profile_user.rooms_set.all()
   topic = Topic.objects.all()
   content = {'user': profile_user,'rooms':room,'topic':topic}
   return render(request,'base/profile.html',content)


@login_required(login_url='login')
def update_user(request):
   return render(request,'base/updateUser.html')

