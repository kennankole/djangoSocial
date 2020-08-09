from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from . models import Profiles

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True, **kwargs):
        user = User
        user_profile = super().save(commit=False)
        if user:
            user_profile.user = user
        if commit:
            user_Profiles.save()
            self.save_m2m()
            Profiles.objects.update_or_create(
                user=user_profile,
                defaults={
                    'slug':slugify(
                        user.username
                    ),
                }
            )
        return user_profile



class ProfilesUpdateForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = (
            'bio', 'profile_pic'
        )