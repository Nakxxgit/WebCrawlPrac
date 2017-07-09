from django.db import models

# Create your models here.

class PostData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    PostNum = models.IntegerField()

    def __str__(self):
    	return self.title