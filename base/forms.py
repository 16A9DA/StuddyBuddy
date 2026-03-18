from django.forms import ModelForm
from .models import Rooms,Message,User
from django.contrib.auth.forms import UserCreationForm

class RoomForm(ModelForm):
    class Meta:
        model  = Rooms
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model  = Message
        fields = ['body']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar","name","username","bio"]


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']