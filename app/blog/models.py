from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000, default='')

    def __str__(self):
        return self.user_pk

class Comment(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000, default='')

    def __str__(self):
        return self.post_id

class Introduction(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=300, default='')
    last_updated = models.DateTimeField(auto_now=True)
