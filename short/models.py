from django.db import models
from django.contrib.auth.models import User

class AnonymousShortify()

# Create your models here.
class Shortify(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.url