from django.db import models

class AnonymousShorti(models.Model):
    url = models.URLField()
    short_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f' {self.url} '
