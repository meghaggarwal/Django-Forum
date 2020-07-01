from .models import Topic
from django import forms

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5 , 'placeholder':'What\'s in your mind?'}
        ), 
    max_length=4000, 
    help_text='Max word limit: 4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']