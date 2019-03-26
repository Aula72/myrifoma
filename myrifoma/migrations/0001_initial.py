# Generated by Django 2.0.2 on 2018-11-15 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('service', models.CharField(choices=[('A', 'Electric Installation'), ('B', 'Laundry'), ('C', 'House Cleaning'), ('D', 'Shopping and Delievery'), ('E', 'Handy Work'), ('F', 'Garden Work'), ('G', 'Interior Painting'), ('H', 'Painting'), ('I', 'Catering'), ('J', 'Helping Carry'), ('K', 'Transportation and Delivery')], max_length=1)),
                ('location', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('company_contact', models.CharField(max_length=13)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('A', 'Electric Installation'), ('B', 'Laundry'), ('C', 'House Cleaning'), ('D', 'Shopping and Delievery'), ('E', 'Handy Work'), ('F', 'Garden Work'), ('G', 'Interior Painting'), ('H', 'Painting'), ('I', 'Catering'), ('J', 'Helping Carry'), ('K', 'Transportation and Delivery')], max_length=1)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]