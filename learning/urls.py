from django.urls import path
from . import views

app_name = 'learning'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),

    path('python/', views.PythonListView.as_view(), name='python'),
    path('python/<int:pk>', views.PythonDetailView.as_view(), name='python_detail'),

    path('django/', views.DjangoListView.as_view(), name='django'),
    path('django/<int:pk>', views.DjangoDetailView.as_view(), name='django_detail'),

    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),

]