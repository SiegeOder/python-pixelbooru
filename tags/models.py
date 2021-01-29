from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=32)
    definition = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.name
