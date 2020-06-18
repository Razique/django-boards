from django import forms

from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind captain?'}
        ),
        max_length=4000,
        help_text='The max length for the text field is 4000 characters.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['message',]
