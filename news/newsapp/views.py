from django.contrib.auth.mixins import PermissionRequiredMixin

from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import PostFilter
from .forms import PostForm
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 3


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'each_news.html'
    context_object_name = 'each_news'


class PostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('newsapp.add_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('newsapp.change_post')
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newsapp.delete_post')
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
