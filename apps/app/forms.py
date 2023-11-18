from django import forms
from apps.post.models import Post

class KittyForm(forms.Form):
    username = forms.CharField(max_length=150, required=False)
    bio = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)


class PostForm(forms.ModelForm):
    category = forms.CharField(max_length=225, required=False, label='Темы (через пробел)')
    class Meta:
        model = Post
        fields = ['title', 'text', 'image'] 

