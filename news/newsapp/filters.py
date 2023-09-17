from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from .models import Post, Category
from django.forms import DateTimeInput

class PostFilter(FilterSet):
    postCategory = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
    )

    date = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            attrs={'type': 'date'},
            format='%Y-%m-%dT',
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'categoryType': ['exact'],
       }