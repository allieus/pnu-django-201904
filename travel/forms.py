from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Comment
from .widgets import TextCounterInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': TextCounterInput,
            'content': SummernoteWidget,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }
