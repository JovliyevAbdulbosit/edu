# Generated by Django 4.0.4 on 2022-05-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_courses_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]