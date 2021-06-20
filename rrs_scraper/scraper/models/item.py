from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.models import TimeStampedModel

from .feed import Feed


class Item(TimeStampedModel):
    """
    Item model, where each feed should have list of items
    """
    STATUS_CHOICES = Choices(
        ('UNREAD', _('Unread')),
        ('READ', _('Read')),
    )
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    summary = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    rights = models.CharField(max_length=200)
    publication_date = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES.UNREAD, max_length=15)

    class Meta:
        verbose_name = 'Item'
        db_table = 'Item'

    def __str__(self):
        return self.title