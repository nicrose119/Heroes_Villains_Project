from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def super_detail(request, pk):
    try:
        super = Supers.objects.get(pk=pk)
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    except Supers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(pk)