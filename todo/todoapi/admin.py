from django.contrib import admin
from todoapi.models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    list_display = ["id","title","description","is_completed"]
