from datetime import datetime

# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from .models import *

bad_names = ['fatty', 'allergies', 'marijuana']

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-dateCreation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context


class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — each_news.html
    template_name = 'each_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'each_news'


# class AuthorsPage(ListView):
#     model = Author  # queryset = Author.objects.all()
#     context_object_name = "Authors"
#     template_name = 'authors.html'


# class PostDetail(View):
#     def get(self, request, pk):
#         ps = Post.objects.get(id=pk)
#         return render(request, "posts.html", {'ps':ps})
#
#
# def news_page_list(request):
#     newslist = Post.objects.all().order_by('-rating')[:6]
#     return render(request, 'news.html', {'newslist': newslist})
#
# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Page not found</h1>')