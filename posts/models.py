from django.db import models
from django.contrib.auth.models import User


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(DomainEntity):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    
    def __str__(self):
        return self.name[:30]
    
    
class Post(DomainEntity):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category")
    title = models.CharField(max_length=50)
    body = models.TextField()
    

    def __str__(self):
        return self.title[:30]
