from wsgiref import validate
from rest_framework import serializers
from todoapi.models import Todo

class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) 
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=300)
    is_completed = serializers.BooleanField(default=False)

    def create(self,validated_data):
        return Todo.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get("title",instance.title)
        instance.description = validated_data.get("description",instance.title)
        instance.is_completed = validated_data.get("is_completed",instance.is_completed)
        instance.save()
        return instance
