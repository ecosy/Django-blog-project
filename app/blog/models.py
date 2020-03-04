from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    subscription_time = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000)

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    contents = models.CharField(max_length=3000)