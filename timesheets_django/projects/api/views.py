from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from .serializers import ProjectSerializer,TaskSerializer
from projects.models import Project, Task
############################################################################################
# Project Related APIs
@swagger_auto_schema(method='post', request_body=ProjectSerializer)
@csrf_exempt
@api_view(['POST'])
def create_project(request):
    if request.method =='POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_projects(request,id=None):
    if request.method =='GET':
        if id is None:
            qs = Project.all_projects.all()
            serializer = ProjectSerializer(qs, many=True)
            return Response(serializer.data,status=HTTP_200_OK)
        qs = Project.all_clients.get(id=id)
        serializer = ProjectSerializer(qs)
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)


# Soft Delete
@swagger_auto_schema(method='delete', request_body=ProjectSerializer)
@api_view(['DELETE'])
def delete_project(request, id):
    if request.method == 'DELETE':
        try:
            qs = Project.all_clients.get(pk=id)
            qs.soft_delete()
            return Response(status=HTTP_200_OK)
        except Project.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ProjectSerializer)
@api_view(['PUT'])
def update_project(request,id):
    try:
        qs = Project.all_clients.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProjectSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def restore_project(request,id):
    try:
        qs = Project.all_deleted_projects.get(pk=id)
    except Project.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        qs.un_delete()
        return Response({'success': 'project successfully restored.'},status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)

    ############################################################################################
    #contact related APIs
@swagger_auto_schema(method='post', request_body=TaskSerializer)
@csrf_exempt
@api_view(['POST'])
def create_task(request):
    if request.method =='POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_tasks(request):
    if request.method =='GET':
        qs= Task.objects.all()
        serializer = TaskSerializer(qs, many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', request_body=TaskSerializer)
@api_view(['DELETE'])
def delete_task(request, id):
    if request.method == 'DELETE':
        try:
            qs = Task.all_tasks.get(pk=id)
            qs.delete()
            return Response(status=HTTP_200_OK)
        except Task.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    return Response(status=HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=TaskSerializer)
@api_view(['PUT'])
def update_task(request,id):
    try:
        qs = Task.all_tasks.get(pk=id)
    except Task.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = TaskSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_400_BAD_REQUEST)
  
