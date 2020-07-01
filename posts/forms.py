from django import forms
from .models import Post


class NewPost(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'id':'post',
        'placeholder' : "what's on your mind",
    }))
    class Meta:
        model = Post
        fields = ['content']