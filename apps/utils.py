import uuid

from django.db import models

class DefaultModelFields(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True, null=False, blank=False, editable=False, unique=True)

    class Meta:
        abstract = True
