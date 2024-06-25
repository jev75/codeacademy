# Generated by Django 5.0.4 on 2024-04-23 11:58

import django.db.models.deletion
import tinymce.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Vardas')),
                ('last_name', models.CharField(max_length=100, verbose_name='Pavardė')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Aprašymas')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Paveikslėlis')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Įveskite knygos žanrą (pvz. detektyvas)', max_length=200, verbose_name='Pavadinimas')),
            ],
            options={
                'verbose_name': 'Žanras',
                'verbose_name_plural': 'Žanrai',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Pavadinimas')),
                ('summary', models.TextField(help_text='Trumpas knygos aprašymas', max_length=1000, verbose_name='Aprašymas')),
                ('isbn', models.CharField(help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>', max_length=13, verbose_name='ISBN')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Viršelis')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.author')),
                ('genre', models.ManyToManyField(help_text='Išrinkite žanrą(us) šiai knygai', to='library.genre')),
            ],
            options={
                'verbose_name': 'Knyga',
                'verbose_name_plural': 'Knygos',
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unikalus ID knygos kopijai', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True, verbose_name='Bus prieinama')),
                ('status', models.CharField(blank=True, choices=[('a', 'Administruojama'), ('p', 'Paimta'), ('g', 'Galima paimti'), ('r', 'Rezervuota')], default='a', help_text='Statusas', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.book')),
            ],
            options={
                'verbose_name': 'Knygos egzempliorius',
                'verbose_name_plural': 'Knygos egzemplioriai',
                'ordering': ['due_back'],
            },
        ),
    ]
