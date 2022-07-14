from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from . import utils

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    # slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        return self.email

    # def generate_random_slug(self):
    #     random_slug = slugify(self.email)
    #     while CustomUser.objects.filter(slug=random_slug).exists:
    #         random_slug = slugify(self.email)
    #     return random_slug

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self.generate_random_slug()
    #     super.save(*args, **kwargs)