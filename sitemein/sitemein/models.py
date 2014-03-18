from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


SITE_TYPE_CHOICES = (
    ("one-page-site", "One page site"),
    ("small-site", "Small site"),
    ("blog", "Blog"),
    ("online-store", "Online store"),
    ("custom", "Custom"),
)

class SiteRequest(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    site_type = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)

    thumb = ImageField(upload_to="thumb", null=True, blank=True)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=500, null=True, blank=True)
    cost = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(SiteRequest, self).save(*args, **kwargs)
