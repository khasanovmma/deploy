# Generated by Django 3.2.1 on 2021-06-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atapp', '0004_alter_teachers_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/teachers/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/news/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]