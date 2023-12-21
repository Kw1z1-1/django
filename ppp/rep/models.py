from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField("name",max_length=50)
    post = models.TextField("description")

    def __str__(self):
        return self.title