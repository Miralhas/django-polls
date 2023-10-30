from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Poll(models.Model):
    title = models.CharField(max_length=128, default="", blank=False)
    poll_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    status = models.BooleanField(null=True, blank=False, default=True)

    @property
    def all_votes(self):
        return self.poll_option.aggregate(Sum('votes'))['votes__sum'] or 0


    def __str__(self):
        return self.title

class Option(models.Model):
    text = models.CharField(max_length=128, default="", blank=False)
    votes = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll_option", blank=True, null=True)

    def __str__(self):
        return f'{self.text} | {self.poll.title}'