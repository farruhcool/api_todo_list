from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ToDo
from .serializers import ToDoSerializer


class ToDoView(APIView):
    def get(self, request):
        todo = ToDo.objects.all()
        serializer = ToDoSerializer(todo, many=True)
        return Response({"todo": serializer.data})

    def post(self, request):
        todo = request.data.get('todo')
        serializer = ToDoSerializer(data=todo, partial=True)
        if serializer.is_valid(raise_exception=True):
            todo_saved = serializer.save()
        return Response({"success": "Todo '{}' created successfully".format(todo_saved.title)})

    def put(self, request, pk):
        saved_todo = get_object_or_404(ToDo.objects.all(), pk=pk)
        data = request.data.get('todo')
        serializer = ToDoSerializer(instance=saved_todo, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            todo_saved = serializer.save()

        return Response({
            "success": "Article '{}' updated successfully".format(todo_saved.title)
        })

    def delete(self, request, pk):
        todo = get_object_or_404(ToDo.objects.all(), pk=pk)
        todo.delete()
        return Response({
            "message": "Todo with id '{}' has been deleted".format(pk)
        }, status=204)
