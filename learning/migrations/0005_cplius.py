# Generated by Django 5.0.4 on 2024-05-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cplius',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=100, verbose_name='Variantas')),
            ],
            options={
                'verbose_name': 'C++',
                'verbose_name_plural': 'C++',
            },
        ),
    ]