# Generated by Django 3.0.4 on 2020-03-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=120)),
                ('dead', models.CharField(max_length=120)),
                ('confirmed', models.CharField(max_length=120)),
                ('recovered', models.CharField(max_length=120)),
            ],
        ),
    ]
