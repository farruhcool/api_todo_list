from django.urls import path

from .views import ToDoView

app_name = "todos"

urlpatterns = [
    path('todos/', ToDoView.as_view()),
    path('todos/<int:pk>', ToDoView.as_view())
]
