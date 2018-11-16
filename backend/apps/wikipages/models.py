from django.db import models

from apps.users.models import User


class WikiPage(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, related_name='wikipages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_updated(self):
        return self.created_at.replace(microsecond=0) != self.updated_at.replace(microsecond=0)

    class Meta:
        verbose_name = 'WikiPage'
        verbose_name_plural = 'WikiPages'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
