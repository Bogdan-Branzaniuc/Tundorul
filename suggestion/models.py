from django.db import models
from tundorul.models import UserProfile


class Suggestions(models.Model):
    title = models.TextField(unique=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='suggestion'
    )
    published_at = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    upvotes = models.ManyToManyField(UserProfile, related_name='upvoted_suggestions', blank=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
