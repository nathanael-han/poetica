from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

class User(AbstractUser):
    picture = models.URLField(null=True, blank=True)


class Poem(models.Model):
    title = models.CharField(max_length=64)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_poems")
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="poems_liked")

    class Meta:
        ordering = ['-created',]

class Comment(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE, related_name="poem_comments")
    comment_body = models.TextField(max_length=256)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")


class Status(models.Model):
    """This class represent a status displayed on the user's profile page"""
    poet = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_status")
    status_body = models.TextField(max_length=256)





