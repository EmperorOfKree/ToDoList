from _datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from todo.forms import TodoModelForm


def index(request):
    todos = Todo.objects.all()

    context = {
        'todos': todos
    }

    return render(request, 'index.html', context)


def add(request):
    form = TodoModelForm(request.POST or None)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=True)
        status = request.POST.get('status')

        if status:
            obj.conclusion_date = datetime.now()

        obj.save()
        return redirect('../../todo/')

    return render(request, 'add.html', context)


def edit(request, id=None):
    form = TodoModelForm(request.POST or None)

    if id:
        todo = get_object_or_404(Todo, pk=id)
        form = TodoModelForm(request.POST or None, instance=todo)

        if request.POST and form.is_valid():
            obj = form.save(commit=True)
            status = request.POST.get('status')
            obj.edit_date = datetime.now()

            if status:
                obj.conclusion_date = datetime.now()

            if "delete" in request.POST:
                obj.delete_date = datetime.now();

            obj.save()
            return redirect('../../todo/')

    context = {'form': form}
    return render(request, 'edit.html', context)

