# Generated by Django 2.1.7 on 2019-03-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descriptiom', models.TextField()),
                ('opening_time', models.TextField()),
                ('min_age_allowed', models.IntegerField()),
            ],
        ),
    ]
