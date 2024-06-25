from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Pavadinimas')
    content = HTMLField(blank=True, null=True, verbose_name='Turinys')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Paveikslėlis')

    class Meta:
        verbose_name = 'Programavimo kalba'
        verbose_name_plural = 'Programavimo kalbos'

    def __str__(self):
        return self.name


class Python(models.Model):
    title = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategorija')
    content = HTMLField(blank=True, null=True, verbose_name='Turinys')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Paveikslėlis')

    class Meta:
        ordering = ['title']
        verbose_name = 'Python'
        verbose_name_plural = 'Python'

    def __str__(self):
        return self.title


class Django(models.Model):
    title = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategorija')
    content = HTMLField(blank=True, null=True, verbose_name='Turinys')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Paveikslėlis')

    class Meta:
        ordering = ['title']
        verbose_name = 'Django'
        verbose_name_plural = 'Django'

    def __str__(self):
        return self.title


class Task(models.Model):
    class QType(models.TextChoices):
        TEXT = 'TXT', 'Tekstas'
        RADIO = 'RADIO', 'Vienas pasirinkimas'
        CHECKBOX = 'CHECKBOX', 'Daug pasirinkimų'

    qtype = models.CharField(max_length=10, choices=QType.choices, default=QType.RADIO, verbose_name='Tipas')
    title = models.CharField(max_length=100, verbose_name='Pavadinimas')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategorija')
    question = HTMLField(blank=True, null=True, verbose_name='Užduotis')

    class Meta:
        ordering = ['title']
        verbose_name = 'Užduotis'
        verbose_name_plural = 'Užduotys'

    def __str__(self):
        return self.title


class Answer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Užduotis')
    option = models.CharField(max_length=100, verbose_name='Variantas')
    is_correct = models.BooleanField(default=False, verbose_name='Teisingas')

    class Meta:
        verbose_name = 'Atsakymas'
        verbose_name_plural = 'Atsakymai'

    def __str__(self):
        return self.option
