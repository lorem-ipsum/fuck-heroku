# Generated by Django 3.0.7 on 2020-06-27 13:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200627_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False),
        ),
    ]