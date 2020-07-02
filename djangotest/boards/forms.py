from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(max_length=4000, help_text='Max limit: 4000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']    