from django import forms
from .models import *

# the class is the name of the form
class PostForm(forms.ModelForm):
    """docstring for PostForm"""

    class Meta:  # in this class we tell django which model should be used
        model = Post
        fields = ('title', 'text')  # we specify which field should end up in our form
        # author should be the person who is currently logged in, created_date should be automatically set


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
