from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.models import TimeStampedModel


class Feed(TimeStampedModel):
    """
    Fee model where each feed has a couple of fields (link, owner, title, ...etc)
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feeds')
    title = models.CharField(max_length=200, null=False, blank=False)
    subtitle = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    link = models.URLField()
    logo = models.ImageField(null=True, blank=True)
    rights = models.CharField(max_length=200)
    last_update = models.DateTimeField(null=True, blank=True)
    followed = models.BooleanField(default=True)
    auto_update = models.BooleanField(default=True)

    class Meta:
        unique_together = ('owner', 'link')
        verbose_name = 'Feed'
        db_table = 'feed'

    def __str__(self):
        return self.title