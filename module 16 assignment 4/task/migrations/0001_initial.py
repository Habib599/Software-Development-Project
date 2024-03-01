# Generated by Django 5.0.1 on 2024-02-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=255)),
                ('task_description', models.TextField(blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('task_assign_date', models.DateField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='categories', to='category.taskcategory')),
            ],
        ),
    ]