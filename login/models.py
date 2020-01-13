from django.db import models
from django.contrib.auth.models import User

USER_TYPE_CHOICES=(
    (1, "Admin"),
    (2, "Accountant"),
    (3, "Stock manager")
)

class User(AbstractUser):
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
