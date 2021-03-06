# Generated by Django 3.0.6 on 2020-05-15 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50)),
                ('category', models.TextField(max_length=100)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
                ('created_by', models.TextField(max_length=50)),
                ('updated_by', models.TextField(max_length=50)),
                ('short_description', models.TextField(max_length=300)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='blogs/images')),
            ],
        ),
    ]
