# Generated by Django 3.2.7 on 2021-09-24 12:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20210924_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photomodel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
