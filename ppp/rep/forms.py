from django.forms import ModelForm, TextInput, Textarea
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'post': Textarea(attrs={'class': 'form-control', 'placeholder': 'description'}),
        }