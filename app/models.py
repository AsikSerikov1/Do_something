from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title