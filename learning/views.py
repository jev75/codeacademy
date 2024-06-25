from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Category, Python, Django, Task
from .forms import AnswerForm

class IndexView(generic.TemplateView):
    template_name = 'learning/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_categories'] = Category.objects.count()
        context['num_python'] = Python.objects.count()
        context['num_django'] = Django.objects.count()
        context['num_tasks'] = Task.objects.count()
        context['num_visits'] = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = context['num_visits'] + 1

        return context

class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'learning/category_list.html'

class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'learning/category_detail.html'

class PythonListView(generic.ListView):
    model = Python
    context_object_name = 'python_list'
    template_name = 'learning/python_list.html'
    paginate_by = 5  # Nustatykite puslapio dydį

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset

class PythonDetailView(generic.DetailView):
    model = Python
    context_object_name = 'python'
    template_name = 'learning/python_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_python'] = Python.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_python'] = Python.objects.filter(id__gt=self.object.id).order_by('id').first()
        return context

class DjangoListView(generic.ListView):
    model = Django
    context_object_name = 'django_list'
    template_name = 'learning/django_list.html'

class DjangoDetailView(generic.DetailView):
    model = Django
    context_object_name = 'django'
    template_name = 'learning/django_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['previous_django'] = Django.objects.filter(id__lt=self.object.id).order_by('-id').first()
        context['next_django'] = Django.objects.filter(id__gt=self.object.id).order_by('id').first()
        return context

class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'learning/task_list.html'

class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'learning/task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answer_choices = [(answer.option, answer.option) for answer in self.object.answer_set.all()]
        context['form'] = AnswerForm(answer_choices=answer_choices)
        next_task = Task.objects.filter(id__gt=self.object.id).order_by('id').first()
        context['next_task_id'] = next_task.id if next_task else None
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        answer_choices = [(answer.option, answer.option) for answer in self.object.answer_set.all()]
        form = AnswerForm(request.POST, answer_choices=answer_choices)

        if form.is_valid():
            answer = form.cleaned_data['answer']
            correct_answers = self.object.answer_set.filter(is_correct=True)
            result, color = self.evaluate_answer(answer, correct_answers)
            next_task = Task.objects.filter(id__gt=self.object.id).order_by('id').first()
            next_task_id = next_task.id if next_task else None
            return render(request, 'learning/result.html',
                          {'result': result, 'color': color, 'next_task_id': next_task_id,
                           'current_task_id': self.object.id})
        else:
            return render(request, 'learning/task_detail.html', {'task': self.object, 'form': form})

    def evaluate_answer(self, answer, correct_answers):
        if any(correct_answer.option == answer for correct_answer in correct_answers):
            return 'Teisingai', 'green'
        else:
            return 'Neteisingai, bandykite dar kartą', 'red'
