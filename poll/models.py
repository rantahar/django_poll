from django.db import models


class Topic(models.Model):
    """ Defines the topics to vote that can be voted for. Each has a
        title, description and of course a vote count.
    """
    title = models.CharField(
        max_length=128,
        unique=True,
    )
    description = models.CharField(max_length=1024)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('votes', )
