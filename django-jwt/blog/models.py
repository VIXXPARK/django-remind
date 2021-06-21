from django.db import models
from django.utils import timezone
from myuser.models import User

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Image(models.Model):
    
    postId=models.ForeignKey(Post,on_delete=models.CASCADE)
    image=models.ImageField()

