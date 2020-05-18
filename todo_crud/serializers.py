from rest_framework import serializers

from .models import ToDo


class ToDoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)
