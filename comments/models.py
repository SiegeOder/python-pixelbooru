from _ast import mod

from django.db import models
from posts.models import Post
from profiles.models import Profile


class Comment(models.Model):
    text = models.CharField(max_length=256)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
