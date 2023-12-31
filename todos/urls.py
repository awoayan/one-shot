from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_list, name="todo_list_list"),
    path("<int:id>/", views.todo_list_detail, name="todo_list_detail"),
    path("<int:id>/edit/", views.todo_list_detail, name="todo_list_detail"),
    path("create/", views.todo_list_create, name="todo_list_create"), 
] 