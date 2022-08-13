from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    
class Search(models.Model):
    name=models.CharField(max_length=100)
    content=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)