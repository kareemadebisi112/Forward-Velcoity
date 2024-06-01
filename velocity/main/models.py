from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Lead(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.CharField(max_length=40)
    message = models.TextField()

    def __str__(self):
        return self.name