from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Portfolio(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='files')

    def __str__(self):
        return self.title
