from django.urls import path
import todoapi.views as tdv

urlpatterns = [

    path("get_todo/", tdv.get_todo, name="get-todo"),

    path("create_todo/", tdv.create_todo, name="create-todo"),

    path("update_todo/<int:id>", tdv.update_todo, name="update-todo"),

    path("delete_todo/<int:id>", tdv.delete_todo, name="delete-todo"),
]