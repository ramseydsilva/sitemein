from django.db import models
from django.contrib.auth.models import User

SITE_TYPE_CHOICES = (
    ("one-page-site", "One page site"),
    ("small-site", "Small site"),
    ("blog", "Blog"),
    ("online-store", "Online store"),
    ("custom", "Custom"),
)

class SiteRequest(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    site_type = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SiteRequest, self).save(*args, **kwargs)
