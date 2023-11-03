from django.db import models
from django.urls import reverse

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('show-detail', args = [str(self.id)])
    