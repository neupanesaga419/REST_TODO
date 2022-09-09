from django.shortcuts import render
from rest_framework.decorators import api_view
from todoapi.serializers import TodoSerializer
from todoapi.models import Todo
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
def get_todo(request):
    is_completed = None
    key = "completed"
    if key in request.GET.keys():
        is_completed = request.GET["completed"]

    if is_completed:
        query = Todo.objects.filter(is_completed=is_completed)
    else:
        query = Todo.objects.all()

    serializer = TodoSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_todo(request):
    if request.method=="POST":
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return_data = {
                "message":"Success"
            }
            return Response(return_data)
        else:
            return Response(serializer.errors)


@api_view(["GET","POST","PUT"])
def update_todo(request,id):
    try:
        query = Todo.objects.get(id=id)
        serializer = TodoSerializer(query)

        if request.method== "POST":
            data = request.data
            serializer = TodoSerializer(instance=query,data=data)
            if serializer.is_valid():
                serializer.save()
                message = {"msg":"data successfully updated"}
                return Response(message)
            else:
                return Response(serializer.errors)
        
        if request.method== "PUT":
            data = request.data
            serializer = TodoSerializer(instance=query,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                message = {"msg":"data successfully updated"}
                return Response(message)
            else:
                return Response(serializer.errors)
        return Response(serializer.data)
    except ObjectDoesNotExist:
        msg = f"The Object with id {id} doesnot exists in db."
        return Response({"msg":msg})


@api_view(["DELETE"])
def delete_todo(request,id):
    try:
        query = Todo.objects.get(id=id)
        query.delete()
        msg = f"The object with id {id} successfully deleted."
        return Response({"msg":msg})
    
    except ObjectDoesNotExist:
        msg = f"The object with id {id} doesnot exists in db."
        return Response({"msg":msg})