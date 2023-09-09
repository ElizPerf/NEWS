from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView
from  django.views.generic.base import View
from .models import *


class AuthorsPage(ListView):
    model = Author  # queryset = Author.objects.all()
    context_object_name = "Authors"
    template_name = 'newsapp/authors.html'


class PostDetail(View):
    def get(self, request, pk):
        ps = Post.objects.get(id=pk)
        return render(request, "newsapp/posts.html", {'ps':ps})


def news_page_list(request):
    newslist = Post.objects.all().order_by('-rating')[:6]
    return render(request, 'newsapp/news.html', {'newslist': newslist})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')