from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
