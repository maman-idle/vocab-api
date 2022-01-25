from django.db import models
from accounts.models import Account

class word(models.Model):
    owner = models.ForeignKey(Account, related_name="word", on_delete=models.CASCADE)
    word = models.CharField(max_length=50, null=False)
    translate = models.CharField(max_length=500, null=False)
