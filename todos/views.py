from django.shortcuts import render, get_object_or_404, redirect
from todos.forms import TodoListForm
from todos.models import TodoList
# Create your views here.


def show_list(request):
    model_list = TodoList.objects.all()
    context = {
        "show_list": model_list,
    }
    return render(request, "todos/list.html", context)


def todo_list_detail(request, id):
    lists = get_object_or_404(TodoList, id=id)
    context = {
        "list_object": lists}
    return render(request, "todos/detail.html", context)


def todo_list_create(request):
    if request.method == "POST" and TodoListForm:
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
    else:
        form = TodoListForm()
    context = {
        "form": form,
    }
    return render(request, "todos/create_list.html", context)