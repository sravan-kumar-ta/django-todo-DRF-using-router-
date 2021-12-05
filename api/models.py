from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Images/', default='Images/default_image.img')

    def __str__(self):
        return self.title
