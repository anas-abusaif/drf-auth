from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
  email = models.EmailField(verbose_name='Email adress',max_length=30, unique=True)
  age = models.IntegerField(verbose_name='Age',blank=True, null=True)
  gender = models.CharField(verbose_name='gender', choices=(('Male','male'),('Female','female')),max_length=10)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"

  def __str__(self) -> str:
    return self.email