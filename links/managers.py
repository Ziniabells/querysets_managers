from django.db import models 
from .models import ActiveLinkManager

class ActiveLinkManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(active=True)

        