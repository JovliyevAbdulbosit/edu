# Generated by Django 4.0.4 on 2022-05-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teachermodel',
            name='profession',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
