from django.urls import path
from . import views


urlpatterns = [ 
    path('deleteMessage/<int:pk>/',views.delete_message,name='deleteMessage'),
    path('editMessage/<int:pk>/',views.update_message,name="update_message"),
    path('register/',views.registerUser,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('login/',views.loginRegister,name="login"),
    path("",views.home,name="Home"),
    path("room/<int:pk>/",views.room,name="room"),
    path("createRoom/",views.create_room,name="createRoom"),
    path("updateRoom/<int:pk>/",views.update_room,name='updateRoom'),
    path("deleteRoom/<int:pk>/",views.delete_room,name="deleteRoom"),
    path('userProfile/<str:username>',views.user_profile,name='userProfile'),
    path('updateProfile/',views.update_user,name='updateUser')
    # make update user settings an option
]

