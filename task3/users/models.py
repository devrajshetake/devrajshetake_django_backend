from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

# class userRegistration(models.Model):
#     username = models.CharField(unique=True, max_length=15)
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     phone = models.IntegerField(unique=True)
#     TYPE_SELECT = (('0', 'Male'),('1', 'Female'),('2','Other'))
#     # gender = ChoiceField(choices=TYPE_SELECT)
#     password1 = models.CharField(max_length=20)
#     password2 = models.CharField(max_length=20)




class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='members')
    phone = models.IntegerField(unique=True)
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),('O','Other')]
    gender = models.CharField(
        max_length = 1,
        choices = GENDER_CHOICES,
        default='F',
        )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.user.username}"
