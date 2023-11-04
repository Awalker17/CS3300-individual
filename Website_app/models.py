from django.db import models
from django.urls import reverse

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=200)
    finished = models.BooleanField(default = False)
    season = models.CharField(max_length=3, blank = True)
    episode = models.CharField(max_length=3, blank = True)
    language = models.CharField(max_length=200, blank = True)
    streaming = models.CharField(max_length=200, blank = True)
    description = models.TextField()
    synopis = models.TextField(blank = True)


    
    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('show-detail', args = [str(self.id)])
    