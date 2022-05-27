from django.conf import settings
from django.db import models
from django.contrib.flatpages.models import FlatPage as CoreFlatPage

# Create your models here.

class MainSite(CoreFlatPage):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="about_us")
    favicon = models.ImageField(upload_to="about_us", verbose_name="Small logo",
                                help_text="20px by 20px", blank=False, null=True)
    site_main_color = models.CharField(max_length=15, blank=True, null=True)
    site_secondary_color = models.CharField(
        max_length=15, blank=True, null=True)
    phone = models.CharField(
        max_length=250, help_text='separate multiple phone numbers with comma')
    email = models.EmailField()
    website = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250, blank=True, null=True)
    twitter = models.CharField(max_length=250, blank=True, null=True)
    instagram = models.CharField(max_length=250, blank=True, null=True)
    youtube = models.CharField(max_length=250, blank=True, null=True)
    whatsapp = models.CharField(max_length=250, blank=True, null=True)
    social_image = models.ImageField(
        upload_to="about_us", help_text="Social media image", blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Main Site"

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots')
    is_author = models.BooleanField()

    def __str__(self):
        return self.name
