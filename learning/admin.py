from django.contrib import admin
from .models import Category, Python, Django, Task, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class TaskAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('title', 'category',)

class PythonAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)

class DjangoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)


admin.site.register(Category)
admin.site.register(Python, PythonAdmin)
admin.site.register(Django, DjangoAdmin)
admin.site.register(Task, TaskAdmin)
