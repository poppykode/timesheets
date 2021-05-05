from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from rest_framework.response import Response
from .serializers import ClientSerializer,ContactSerializer
from clients.models import Client, Contact

############################################################################################
# Client Related APIs
@swagger_auto_schema(method='post', request_body=ClientSerializer)
@csrf_exempt
@api_view(['POST'])
def create_client(request):
    if request.method =='POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_clients(request,id=None):
    if request.method =='GET':
        if id is None:
            qs = Client.all_clients.all()
            serializer = ClientSerializer(qs, many=True)
            return Response(serializer.data,status=HTTP_200_OK)
        qs = Client.all_clients.get(id=id)
        serializer = ClientSerializer(qs)
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)


# Soft Delete
@swagger_auto_schema(method='delete', request_body=ClientSerializer)
@api_view(['DELETE'])
def delete_client(request, id):
    if request.method == 'DELETE':
        try:
            qs = Client.all_clients.get(pk=id)
            qs.soft_delete()
            return Response(status=HTTP_200_OK)
        except Client.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ClientSerializer)
@api_view(['PUT'])
def update_client(request,id):
    try:
        qs = Client.all_clients.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ClientSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def restore_client(request,id):
    try:
        qs = Client.all_deleted_clients.get(pk=id)
    except Client.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        qs.un_delete()
        return Response({'success': 'client successfully restored.'},status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)

    ############################################################################################
    #contact related APIs
@swagger_auto_schema(method='post', request_body=ContactSerializer)
@csrf_exempt
@api_view(['POST'])
def create_contact(request):
    if request.method =='POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_contact(request):
    if request.method =='GET':
        qs= Contact.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', request_body=ContactSerializer)
@api_view(['DELETE'])
def delete_contact(request, id):
    if request.method == 'DELETE':
        try:
            qs = Contact.objects.get(pk=id)
            qs.delete()
            return Response(status=HTTP_200_OK)
        except Contact.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ContactSerializer)
@api_view(['PUT'])
def update_contact(request,id):
    try:
        qs = Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ContactSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)
  
