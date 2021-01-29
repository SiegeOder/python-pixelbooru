from django.db import models
from profiles.models import Profile
from tags.models import Tag
from time import strftime
from datetime import datetime


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{str(datetime.now()).split()[-1].replace(":", "_")}.{ext}'
    return f'{strftime("images/posts/%Y/%m/%d")}/{filename}'


class Post(models.Model):
    # name = models.CharField(max_length=32)
    image = models.ImageField(upload_to=get_file_path, default='images/posts/noimage.png')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.image)
