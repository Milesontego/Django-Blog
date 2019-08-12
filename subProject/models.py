from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    picture = models.ImageField(default="default.jpg", upload_to="post_images")
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return f"post by {self.author} called {self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField()
    reply = models.ForeignKey('self', null=True, on_delete=models.CASCADE ,related_name='replies')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment for __{self.post.title}__ from this guy called __{self.user.username}__"





class feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name



