# Generated by Django 5.0.4 on 2024-04-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profilis', 'verbose_name_plural': 'Profiliai'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name='Profilio nuotrauka'),
        ),
    ]
