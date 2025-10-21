from django.contrib.auth.models import User

from django.db import models

class Book (models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    cover = models.ImageField(upload_to="book_cover/", null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,
        null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
