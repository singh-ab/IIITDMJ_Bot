# Generated by Django 4.2 on 2023-04-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseAPI', '0002_remove_student_id_alter_student_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('about', models.TextField(max_length=5000)),
            ],
        ),
    ]
