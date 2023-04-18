from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_list, name="todo_list_list"),
    path("<int:id>/", views.todo_list_detail, name="todo_list_detail"),
]