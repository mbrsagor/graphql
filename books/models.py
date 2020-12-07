from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:30]


class Todo(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:50]
