from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Rooms
from .serializers import RoomSerializer
@api_view(['GET'])

def getRoutes(request):
    routes = [
        "GET /api",
        "GET /api/room",
        "GET /api/room/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    room = Rooms.objects.all()
    serlizer = RoomSerializer(room,many=True)
    return Response(serlizer.data)


@api_view(['GET'])
def getRoom(request,pk):
    room = Rooms.objects.get(id=pk)
    serlizer = RoomSerializer(room,many=False)
    return Response(serlizer.data)