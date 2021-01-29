from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/users', default='images/users/guest.png')
    note = models.CharField(max_length=128, null=True)
    role = models.CharField(max_length=16, default='user')

    def __str__(self):
        return self.user.username
