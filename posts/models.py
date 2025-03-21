from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('DRAFT', 'Draft'), ('PUBLISHED', 'Publish'))
    title=models.CharField(max_length=30)
    slug=models.SlugField(max_length=30)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')

