from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)
    class Meta:
        model = Post
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get('title'
                                 '')
        if text == title:
            raise ValidationError(
                'Text must not be similar to title'
            )

        return cleaned_data
