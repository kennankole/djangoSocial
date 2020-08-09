from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

User = get_user_model()

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=100,default='hello world')
    profile_pic = models.ImageField(blank=True, null=True)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("public_profile_detail", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse('profile_update')