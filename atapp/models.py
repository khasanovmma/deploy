from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/news/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано!!!')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Teachers(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    photo = models.ImageField(upload_to='photos/teachers/%Y/%m/%d/', verbose_name='Фото', blank=True)
    degree = models.CharField(max_length=150, verbose_name='Ученые звание', blank=True)
    rank = models.CharField(max_length=150, verbose_name='Учёное степень')
    email = models.EmailField(max_length=150, verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учители'


class FeedBackViews(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ф.И.О.')
    email = models.EmailField(max_length=150, verbose_name='Электронная почта')
    desc = models.CharField(max_length=1000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    class Meta:
        verbose_name = 'Oбратная связь'
        verbose_name_plural = 'Oбратная связь'


class Table(models.Model):
    table = models.FileField(upload_to='documats/table/%Y/%m/%d/', max_length=10000, verbose_name='График')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'График'
