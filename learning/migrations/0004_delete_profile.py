# Generated by Django 5.0.4 on 2024-04-28 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_alter_profile_options_alter_profile_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
