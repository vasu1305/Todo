from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/tasks/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of tasks'
        },
        {
            'Endpoint': '/task/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns single tasks object'
        },
        {
            'Endpoint': '/add/',
            'method': 'POST',
            'body': {"tasks": ""},
            'description': 'Creates new task with data sent in post request'
        },
        {
            'Endpoint': '/update/id/',
            'method': 'PATCH',
            'body': {"tasks": ""},
            'description': 'Creates an existing task with data sent in post request'
        },
        {
            'Endpoint': '/delete/id/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing task'
        },
    ]
    return Response(routes)



class TaskApi(APIView):
    def get(self, request, *args, **kwargs):
        task  = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(task, many=True)
        identity = [{'user': request.user}]
        return Response(serializer.data, identity)

    def get(self, request, id=id, *args, **kwargs):
        task  = get_list_or_404(Todo, id=request.GET.get('id'))
        serializer = TodoSerializer(task)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, id=id):
        task  = get_list_or_404(Todo, id=request.GET.get('id'))
        serializer = TodoSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=id):
        id = request.GET.get('id')
        task = Todo.objects.get(id=id)
        task.delete()
        return Response('Task was deleted')
        
# @api_view(['GET'])
# def get(request, id=None):
#     if id is not None:
#         task  = get_list_or_404(Todo, id=id)
#         serializer = TodoSerializer(task, many=True)
#         identity = [{'user': request.user}]
#         return Response(serializer.data)
#     task  = get_list_or_404(Todo)
#     serializer = TodoSerializer(task, many=True)
#     identity = [{'user': request.user}]
#     return Response(serializer.data)

# @api_view(['POST'])
# def post(request):
#     serializer = TodoSerializer(data=request.data, many=False)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response("Error")

# @api_view(['PATCH'])
# def patch(request, id):
#     task = Todo.objects.get(id=id)
#     serializer = TodoSerializer(task, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response("Error")

# @api_view(['DELETE'])
# def delete(request, id):
#     task = Todo.objects.get(id=id)
#     task.delete()
#     return Response('Task was deleted')
