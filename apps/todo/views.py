from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View

from apps.todo.forms import AddTaskModelForm, AddCategoryModelForm
from apps.todo.models import Category, Task


class ListTask(ListView):  # list of task
    model = Task
    context_object_name = 'task_list'


class DetailTask(DetailView):  # show detail of task
    model = Task
    template_name = 'todo/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ListCategory(ListView):  # list of category
    model = Category
    context_object_name = 'category_list'


class ListTaskCategory(DetailView):  # list task of category
    model = Category
    template_name = 'todo/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LatestTask(TemplateView):
    template_name = 'todo/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_Task'] = Task.objects.all()[:3]
        return context


class ListTaskDue(ListView):  # list task that deed date
    template_name = 'index.html'


class AddTask(View):  # a form for add task
    def get(self, request):
        form = AddTaskModelForm()
        # form = RegisterPersonModelForm(request.POST)
        return render(request, 'todo/add_task.html', {'form': form})

    def post(self, request):
        # print("request.POST: {}".format(request.POST))
        # form = RegisterPersonModelForm(request.POST)
        form = AddTaskModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            person_obj = Task(**validated_data)
            print(person_obj)
            person_obj.save()
            return redirect('ok')
        return render(request, 'todo/add_category.html', {'form': form})


class AddCategory(View):  # a form for add category
    def get(self, request):
        form = AddCategoryModelForm()
        return render(request, 'todo/add_category.html', {'form': form})

    def post(self, request):
        form = AddCategoryModelForm(request.POST)
        if form.is_valid():
            validated_data = form.cleaned_data
            person_obj = Category(**validated_data)
            print(person_obj)
            person_obj.save()
            return redirect('ok')
        return render(request, 'todo/add_task.html', {'form': form})
