from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ship, Position
from .serializer import ShipsSerializer, PositionSerializer


def error_message(item):
    return {"error": "Item '{}' not found".format(item)}


@api_view()
def ships_list(request):
    ships = Ship.objects.all()
    return Response(ShipsSerializer(ships, many=True).data)


@api_view()
def ships_position(request, imo):
    result = None
    try:
        ship = Ship.objects.get(imo=imo)
    except Ship.DoesNotExist:
        result = error_message(imo)

    else:
        positions = (Position.objects.filter(imo=ship.pk)
                     .order_by('-timestamp'))
        result = PositionSerializer(positions, many=True).data
    return Response(result)
