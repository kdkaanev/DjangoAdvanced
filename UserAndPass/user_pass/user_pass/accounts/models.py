from django.contrib.auth import get_user_model, models as auth_models
from django.db import models

# Create your models here.

UserModel = get_user_model()


class AccountUser(auth_models.AbstractUser):
    age = models.IntegerField(
        blank=False,
        null=False,
    )
