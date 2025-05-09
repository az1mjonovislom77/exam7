# Generated by Django 5.2 on 2025-04-18 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_module_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='module',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
