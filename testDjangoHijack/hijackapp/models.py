# Adds for the hijack tuts - by Mark
from django.contrib.auth.models import AbstractUser
from django.db import models

# User class wil inherit from AbstractUserand get all its fields.
class User(AbstractUser):

    # Add foreignKey called next_of_kin, is gonna be a self-referential foreign key from the user to another user model.
    # The 'self' will link the user model to another user model
    next_of_kin = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
