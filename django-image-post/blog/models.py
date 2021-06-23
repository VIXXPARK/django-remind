from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.title

class Image(models.Model):
    blogId=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(default='media/제목없음.jpeg',upload_to="")

    def __str__(self):
        return self.image
