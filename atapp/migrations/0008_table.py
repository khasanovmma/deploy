# Generated by Django 3.2.1 on 2021-06-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atapp', '0007_rename_feedback_feedbackviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.FileField(max_length=10000, upload_to=None, verbose_name='График')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
            ],
            options={
                'verbose_name': 'График',
                'verbose_name_plural': 'График',
            },
        ),
    ]
