# Generated by Django 2.1.7 on 2019-03-31 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20190331_0047'),
        ('core', '0004_place_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='location.Location'),
            preserve_default=False,
        ),
    ]