# Generated by Django 4.2 on 2023-04-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]