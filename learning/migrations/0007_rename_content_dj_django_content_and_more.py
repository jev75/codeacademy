# Generated by Django 5.0.6 on 2024-05-15 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0006_delete_cplius'),
    ]

    operations = [
        migrations.RenameField(
            model_name='django',
            old_name='content_dj',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='python',
            old_name='content_py',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='task',
            name='image',
        ),
    ]
