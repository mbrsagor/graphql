from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:30]
