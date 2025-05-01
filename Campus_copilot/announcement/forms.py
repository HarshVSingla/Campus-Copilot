
from django import forms
from .models import Announcement, Category

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content', 'category', 'author', 'important']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }