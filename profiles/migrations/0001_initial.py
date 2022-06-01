# Generated by Django 3.2.7 on 2022-06-01 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='fotos')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=4096)),
                ('city', models.TextField(max_length=4096)),
                ('zipcode', models.IntegerField(default=0)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Profile1', to='profiles.profile')),
                ('profile2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Profile2', to='profiles.profile')),
            ],
        ),
    ]
