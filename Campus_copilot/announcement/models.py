from django.db import models
from django.utils import timezone

class Category(models.TextChoices):
    ACADEMIC = 'academic', 'Academic'
    EVENT = 'event', 'Event'
    ADMINISTRATIVE = 'administrative', 'Administrative'
    CAREER = 'career', 'Career'
    GENERAL = 'general', 'General'

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.GENERAL
    )
    date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    important = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']