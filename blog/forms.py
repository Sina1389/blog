from django import forms
from .models import Post,Category,Comment

# choices = [('coding', 'coding'),('sports', 'sports'),('entertaiment', 'entertaiment')]
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', "snippet", "header_image")

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TITLE'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TAG'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type':'hidden'}),
            # 'author' : forms.Select(attrs={'class': 'form-control', 'id': 'author'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'AUTHOR'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'BODY'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet', )

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TITLE'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TAG'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control', 'placeholder': 'AUTHOR'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'BODY'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'SNIPPET'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            # 'name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'BODY'}),
        }