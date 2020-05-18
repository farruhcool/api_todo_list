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
        serializer = ToDoSerializer(data=todo)
        if serializer.is_valid(raise_exception=True):
            todo_saved = serializer.save()
        return Response({"success": "Todo '{}' created successfully".format(todo_saved.title)})
