from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import FeedBack
from .models import News, Teachers, FeedBackViews, Table


def index(request):
    news = News.objects.get_queryset().order_by('-id')
    teachers = Teachers.objects.get_queryset().order_by('id')
    tables = Table.objects.all()

    # news
    news_pagination = Paginator(news, 3)
    page_num = request.GET.get('page')
    page = news_pagination.get_page(page_num)
    page_range = news_pagination.page_range

    # teachers content
    teachers_pagination = Paginator(teachers, 2)
    teachers_num = request.GET.get('teachers')
    teachers_page = teachers_pagination.get_page(teachers_num)
    teachers_range = teachers_pagination.page_range

    if request.method == 'POST':
        form = FeedBack(request.POST)
        if form.is_valid():
            FeedBackViews.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(reverse("home"))

    else:
        form = FeedBack()
    context = {
        'page_range': page_range,
        'page': page,
        'teachers_range': teachers_range,
        'teachers_page': teachers_page,
        'form': form,
        'tables': tables
    }
    return render(request, 'dist/index.html', context)
