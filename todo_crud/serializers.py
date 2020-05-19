from rest_framework import serializers

from .models import ToDo


class ToDoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    created_date = serializers.CharField()
    start_date = serializers.CharField()
    end_date = serializers.CharField()
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return ToDo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance
