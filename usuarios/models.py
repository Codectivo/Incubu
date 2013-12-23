from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    """Account class is the model for user accounts."""
    description = models.TextField(max_length=100)
    user_account = models.CharField(max_length=100, verbose_name='user account')
    pass_account = models.CharField(max_length=100, verbose_name='pass_account')
    user = models.ForeignKey(User)
